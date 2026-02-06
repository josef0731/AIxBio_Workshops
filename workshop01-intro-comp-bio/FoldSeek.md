# FoldSeek practical (around 45 minutes)

1.	Introduction to FoldSeek (and structure comparison) (c. 10-15 min, very brief background presentation)
*	DALI
*	TM-align and TM-score
*	FoldSeek for structure comparison at scale
*	How? Structure alphabet (3Di)

Followed by around 30-35 mins of examples. The participants will try these out themselves and we will explain the results (and how to interpret – here this will be checking the scores returned, structure inspection etc.)

2.	FoldSeek examples
*	PDB 2uwi (TNF receptor mimic). FoldSeek top hits are all human/mouse TNF receptors
*	Explanation of the search databases
*	PDB 6eqg (PET hydrolase). Good example of low Seq ID% hits
3.	FoldMason
*	I have a set of coronavirus spike models (around 20) - FoldMason does quite a good job to generate a structure alignment (to share the structures in a ZIP beforehand)
*	Also good to illustrate how 3Di alignment looks like (see web browser)
4.	FoldSeek-Multimer
*	PDB 1j7v (IL10-IL10RA complex) --> FoldSeek-Multimer returns IL-19 and IL-20 with their receptors (all belong to the same IL-10 superfamily)
5.	FoldDisco
*	PDB 3e1u (APOBEC3G bound to zinc). Simple example to look at metal binding site – Zn2+ coordination is simple (only 3 residues involved). FoldDisco search return similar deaminases as expected (but also other proteins with zinc binding sites e.g. zinc fingers)
*	PDB 5o12 and 4eon: both are kinases bound to an inhibitor Ro-3306. Ro-3306 is a CDK1 inhibitor, with bound structures to CDK2 (PDB 4eon). PDB 5o12 is the same inhibitor but bound to an off-target kinase PIM1. FoldDisco search starting from either structure will return the other kinase (as well as a bunch of others)!
