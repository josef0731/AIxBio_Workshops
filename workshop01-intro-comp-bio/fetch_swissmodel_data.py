#!/usr/bin/env python3
"""
Script to fetch SwissModel structure data for Uniprot IDs
"""

import requests
import pandas as pd
import time
from typing import List, Dict, Any


def fetch_swissmodel_data(uniprot_id: str, uniprot_name: str) -> List[Dict[str, Any]]:
    """
    Fetch structure data from SwissModel for a given Uniprot ID.
    
    Args:
        uniprot_id: Uniprot identifier
        
    Returns:
        List of dictionaries containing summary data for each structure
    """
    url = f"https://swissmodel.expasy.org/3d-beacons/uniprot/summary/{uniprot_id}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract summary information from each structure
        results = []
        if 'structures' in data:
            for structure in data['structures']:
                if 'summary' in structure:
                    summary = structure['summary']
                    # Filter for coverage >= 50% and QMEANDisco score exists
                    if summary.get('coverage') >= 0.5 and summary.get('confidence_type') == 'QMEANDisCo': 
                        results.append({
                            'uniprot_id': uniprot_id,
                            'uniprot_name': uniprot_name,
                            'confidence_avg_local_score': summary.get('confidence_avg_local_score'),
                            'confidence_type': summary.get('confidence_type'),
                            'coverage': summary.get('coverage'),
                            'model_identifier': summary.get('model_identifier'),
                            'model_url': summary.get('model_url'),
                            'uniprot_start': summary.get('uniprot_start'),
                            'uniprot_end': summary.get('uniprot_end')
                        })
        
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {uniprot_id}: {e}")
        return []


def process_uniprot_ids(uniprot_entries: List[str], delay: float = 0.5) -> pd.DataFrame:
    """
    Process a list of Uniprot IDs and compile results into a DataFrame.
    
    Args:
        uniprot_entries: List of tuples: (uniprot_id, uniprot_name)
        delay: Delay between requests in seconds (to be respectful to the server)
        
    Returns:
        pandas DataFrame with structure information
    """
    all_results = []
    
    for i, entry in enumerate(uniprot_entries, 1):
        uniprot_id, uniprot_name = entry
        print(f"Processing {i}/{len(uniprot_entries)}: {uniprot_id}")
        results = fetch_swissmodel_data(uniprot_id, uniprot_name)
        # get the one with highest confidence_avg_local_score
        results = sorted(results, key=lambda x: x['confidence_avg_local_score'], reverse=True)[:1]
        all_results.extend(results)
        
        # Add a small delay between requests to be respectful to the server
        if i < len(uniprot_entries):
            time.sleep(delay)
    
    # Create DataFrame
    df = pd.DataFrame(all_results)
    
    return df


if __name__ == "__main__":
    # read in uniprot search results ('Spike protein' and Taxonomy contains 'coronavirus')
    uniprot_search_file = 'uniprotkb_Spike_protein_AND_taxonomy_na_2026_02_06_trimmed.txt'
    unprot_df = pd.read_csv(uniprot_search_file, sep='\t')
    uniprot_entries = list(zip(unprot_df['Entry'], unprot_df['Entry Name']))

    # Process the IDs
    df = process_uniprot_ids(uniprot_entries)
    
    # Display results
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    print(f"\nTotal structures found: {len(df)}")
    print(f"\nDataFrame shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
    
    # Save to CSV
    output_file = "swissmodel_structures.csv"
    df.to_csv(output_file, index=False)
    print(f"\nResults saved to: {output_file}")
    
    # Display summary statistics
    if not df.empty:
        print("\n" + "="*80)
        print("SUMMARY STATISTICS")
        print("="*80)
        print(f"\nStructures per Uniprot ID:")
        print(df['uniprot_id'].value_counts())
        
        if 'coverage' in df.columns and df['coverage'].notna().any():
            print(f"\nAverage coverage: {df['coverage'].mean():.2%}")
        
        if 'confidence_avg_local_score' in df.columns and df['confidence_avg_local_score'].notna().any():
            print(f"Average confidence score: {df['confidence_avg_local_score'].mean():.2f}")

    # Download the model and rename to include UniProt ID and Uniprot name
    for _, row in df.iterrows():
        model_url = row['model_url']
        uniprot_id = row['uniprot_id']
        uniprot_name = row['uniprot_name']
        # substitute '/' in model_identifier with '-' to avoid issues in filenames
        model_identifier = row['model_identifier'].replace('/', '-')
        
        try:
            model_response = requests.get(model_url, timeout=10)
            model_response.raise_for_status()
            filename = f"{uniprot_name}_{model_identifier}.cif"
            with open(filename, 'wb') as f:
                f.write(model_response.content)
            print(f"Downloaded model for {uniprot_id} and saved as {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading model for {uniprot_id}: {e}")        
