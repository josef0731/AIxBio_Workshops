# Workshop 1: Introduction to computational biology: databases and tools

Date: 18th February 2026 (Wed)

Time: 14:00-17:00

Venue: Darwin B05

## Agenda
14:00-14:20 Background & Introduction to the workshops (Joseph)

14:20-15:00 FoldSeek (Joseph + Gorka)

15:00-15:15 Break

15:15-16:15 TED

16:15-17:00 Networking (Coffee & Cake)

## Resources
`FoldSeek.md`: plan for the FoldSeek part of the workshop with examples

`Spike_structures.zip`: with mmCIF files of a bunch of coronavirus spike protein structure models (just 1 chain) for testing FoldMason. I extracted just one chain because FoldMason performs structure comparison for every chain in the structures you supply.

`extract_chain_a.py`: Code (from Claude!) to extract chain A from the downloaded structures (all trimer models)

`fetch_swissmodel_data.py`: Code (from Claude!) that uses the SWISS-MODEL API to obtain models.

`uniprotkb_Spike_protein_AND_taxonomy_na_2026_02_06_trimmed.txt`: My uniprot search results of the coronavirus Spike proteins. Trimmed a little bit to make up a manageable number of structures to run FoldMason online (n=21)
