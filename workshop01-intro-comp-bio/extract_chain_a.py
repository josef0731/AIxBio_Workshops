#!/usr/bin/env python3
"""
Script to extract chain A from mmCIF files 
"""

import os
from pathlib import Path


def extract_chain_from_mmcif(input_file: str, output_file: str, chain_id: str = 'A') -> bool:
    """
    Extract a specific chain from an mmCIF file.
    
    Args:
        input_file: Path to input mmCIF file
        output_file: Path to output mmCIF file
        chain_id: Chain identifier to extract (default: 'A')
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        output_lines = []
        in_atom_site_loop = False
        atom_site_columns = []
        chain_col_idx = None
        auth_asym_col_idx = None
        
        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\n')
            
            # Check if we're starting the atom_site loop
            if line.strip() == 'loop_':
                # Peek ahead to see if next line is _atom_site
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('_atom_site.'):
                    in_atom_site_loop = True
                    output_lines.append(line)
                    atom_site_columns = []
                    chain_col_idx = None
                    auth_asym_col_idx = None
                    i += 1
                    
                    # Read all column definitions
                    while i < len(lines) and lines[i].strip().startswith('_atom_site.'):
                        col_line = lines[i].rstrip('\n')
                        output_lines.append(col_line)
                        atom_site_columns.append(col_line.strip())
                        
                        # Find the chain identifier columns
                        if '_atom_site.label_asym_id' in col_line:
                            chain_col_idx = len(atom_site_columns) - 1
                        if '_atom_site.auth_asym_id' in col_line:
                            auth_asym_col_idx = len(atom_site_columns) - 1
                        
                        i += 1
                    
                    # Now process the data rows
                    atom_lines = []
                    while i < len(lines):
                        data_line = lines[i].rstrip('\n')
                        
                        # Check if we've exited the loop (empty line, #, or new loop_/data_)
                        if (not data_line.strip() or 
                            data_line.strip().startswith('#') or 
                            data_line.strip().startswith('loop_') or
                            data_line.strip().startswith('data_') or
                            data_line.strip().startswith('_')):
                            break
                        
                        # Parse the data line
                        fields = data_line.split()
                        
                        # Check if this row belongs to the target chain
                        keep_row = False
                        if chain_col_idx is not None and len(fields) > chain_col_idx:
                            if fields[chain_col_idx] == chain_id:
                                keep_row = True
                        elif auth_asym_col_idx is not None and len(fields) > auth_asym_col_idx:
                            if fields[auth_asym_col_idx] == chain_id:
                                keep_row = True
                        
                        if keep_row:
                            atom_lines.append(data_line)
                        
                        i += 1
                    
                    # Add the filtered atom lines
                    output_lines.extend(atom_lines)
                    in_atom_site_loop = False
                    
                    # Don't increment i again as we've already processed through the loop
                    continue
                else:
                    # It's a different loop, keep it as is
                    output_lines.append(line)
            else:
                # Not in atom_site loop, keep the line
                output_lines.append(line)
            
            i += 1
        
        # Write output file
        with open(output_file, 'w') as f:
            f.write('\n'.join(output_lines))
            f.write('\n')  # Add final newline
        
        return True
        
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        import traceback
        traceback.print_exc()
        return False


def process_directory(input_dir: str, output_dir: str, chain_id: str = 'A', pattern: str = '*.cif'):
    """
    Process all mmCIF files in a directory and extract specified chain.
    
    Args:
        input_dir: Directory containing input mmCIF files
        output_dir: Directory for output files
        chain_id: Chain identifier to extract (default: 'A')
        pattern: File pattern to match (default: '*.cif')
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all mmCIF files
    input_path = Path(input_dir)
    cif_files = list(input_path.glob(pattern))
    
    if not cif_files:
        print(f"No files matching '{pattern}' found in {input_dir}")
        return
    
    print(f"Found {len(cif_files)} mmCIF files")
    print(f"Extracting chain {chain_id}...\n")
    
    success_count = 0
    fail_count = 0
    
    for cif_file in cif_files:
        input_file = str(cif_file)
        output_file = os.path.join(output_dir, f"{cif_file.stem}_chain{chain_id}.cif")
        
        print(f"Processing: {cif_file.name}")
        
        if extract_chain_from_mmcif(input_file, output_file, chain_id):
            success_count += 1
            print(f"  ✓ Saved to: {output_file}")
        else:
            fail_count += 1
            print(f"  ✗ Failed")
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Successfully processed: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    # Example usage
    # Modify these paths to match your directory structure
    
    input_directory = "."  # Current directory
    output_directory = "./chain_a_extracted"
    
    # Process all .cif files in the input directory
    process_directory(
        input_dir=input_directory,
        output_dir=output_directory,
        chain_id='A',
        pattern='*.cif'
    )
    
    # Alternative: process single file
    # extract_chain_from_mmcif('input.cif', 'output_chainA.cif', 'A')