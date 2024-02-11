# alz_risk_analysis

This program compares two gene sequences for similarity. The program compares a region of the gene sequence of one gene with every region of the gene sequence of another gene. The program accesses the protein-coding genetic sequences from the NCBI Database using the accession numbers of the genes. 

To run this program, find two genes from the NCBI Database and add their accession numbers to the variable 'id' in the fetch_gene1() and fetch_gene2() functions. The program will only retreive the gene sequence when given an accession number starting with 'NM'. 

To find the similarity between the regions of genes, the program uses the pairwise2 global alignment function in BioPython. 

Before calculating the similarity between the regions of genes, the program prints the names of the genes and their descriptions, The program prints each region before comparing them. 

For each pair of regions, pairwise2 function produces multiple global alignments to to produce a similarity score. 
After producing multiple different alignments on a pair of regions, the program prints "Comparison Finished!" in red. 
