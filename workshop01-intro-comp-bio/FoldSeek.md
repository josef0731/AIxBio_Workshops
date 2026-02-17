# FoldSeek practical (around 45 minutes)

*Joseph Ng, February 2026*

Below are a list of examples that illustrate the use of FoldSeek (and its associated tools FoldSeek-Multimer, FoldDisco and FoldMason). Please feel free to try this out yourselves. We will provide explanation on how to run them and how to interpret the results - please feel free to ask for help if you need it!

1.	FoldSeek examples

  * A Tumour Necrosis Factor (TNF) receptor mimic from Cowpox virus: PDB [2uwi](https://www.ebi.ac.uk/pdbe/entry/pdb/2uwi). Make a note of what FoldSeek's top hits are. We will also take this opportunity to explain and discuss the different search databases available on FoldSeek.
  * A Polyethylene terephthalate (PET) degrading hydrolase from *Ideonella sakaiensis*: PDB [6eqg](https://www.ebi.ac.uk/pdbe/entry/pdb/6eqg). Pay attention to sequence identities of the hits returned (in different databases) and appreciate the structural similarity of the top hits.
    
2.	FoldMason

Typically to run FoldMason you'd want a list of structures (/models) rather than just 2 or 3. I have made a set of coronavirus spike protein models (n=22) available here in this repository ([link](https://github.com/josef0731/AIxBio_Workshops/raw/refs/heads/main/workshop01-intro-comp-bio/Spike_structures.zip)). 

Try to upload them to FoldMason and see how the structure alignment would look like. Also take a look at the sequence alignment view including toggles to view the 3Di instead of conventional amino acid alignment. ([Click here for my example result](https://search.foldseek.com/result/foldmason/GhRMKO0K_RDRwDNyLJV-53JXdYivmdkM0Fq9Fw))

3.	FoldSeek-Multimer

  *	Human IL10-IL10RA complex: PDB [1j7v](https://www.ebi.ac.uk/pdbe/entry/pdb/1j7v). IL-10 belongs to a superfamily of cytokine sharing structural similarity with a few others (e.g. IL-19). Take a look and see what complexes FoldSeek-Multimer manages to find!

5.	FoldDisco

  *	First example is to find proteins with zinc binding sites: PDB [3e1u](https://www.ebi.ac.uk/pdbe/entry/pdb/3e1u) (APOBEC3G bound to zinc). Zn2+ coordination is simple (only 3 residues involved). Take a look at the types of proteins FoldDisco search return.
  *	PDB [5o12](https://www.ebi.ac.uk/pdbe/entry/pdb/5o12) and [4eon](https://www.ebi.ac.uk/pdbe/entry/pdb/4eon): both are kinases bound to an inhibitor Ro-3306. Ro-3306 is a cyclin-dependent kinase (CDK) inhibitor, with bound structures to CDK2 (PDB 4eon). PDB 5o12 is the same inhibitor but bound to an off-target kinase PIM1. Try running FoldDisco search starting from either structure and see what it manages to find!
