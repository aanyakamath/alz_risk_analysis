import os
import subprocess
from Bio import Entrez, SeqIO

# Download sequences from NCBI
def download_sequence(seq_id, output_file, db="nucleotide", email="your.email@example.com"):
    Entrez.email = email
    handle = Entrez.efetch(db=db, id=seq_id, rettype="fasta", retmode="text")
    seq_record = SeqIO.read(handle, "fasta")
    handle.close()
    SeqIO.write(seq_record, output_file, "fasta")
    print(f"Downloaded {seq_id} to {output_file}")

# sequence IDs
genome_dir = "genome_index"
dna_seq_id = "NC_000014.9"
mrna_seq_id = "NM_000021.4"
dna_fasta_file = "Homo_sapiens_GRCh38_dna.fasta"
mrna_fasta_file = "Homo_sapiens_GRCh38_mrna.fasta"
output_dir = "star_output"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Download sequences
download_sequence(dna_seq_id, dna_fasta_file)
download_sequence(mrna_seq_id, mrna_fasta_file)

# Function to generate the genome index
def generate_genome_index():
    star_index_command = [
        "STAR",
        "--runMode", "genomeGenerate",
        "--genomeDir", genome_dir,
        "--genomeFastaFiles", dna_fasta_file,
        "--runThreadN", "4"
    ]
    subprocess.run(star_index_command, check=True)
    print("Genome index generation completed successfully.")

# Function to align the mRNA sequence to the DNA
def align_mrna_to_dna():
    star_align_command = [
        "STAR",
        "--genomeDir", genome_dir,
        "--readFilesIn", mrna_fasta_file,
        "--outFileNamePrefix", os.path.join(output_dir, "output_"),
        "--runThreadN", "4",
        "--outSAMtype", "BAM", "SortedByCoordinate"
    ]
    subprocess.run(star_align_command, check=True)
    print("mRNA alignment completed successfully.")

# Generate the genome index (only if not already done)
if not os.path.exists(os.path.join(genome_dir, "SA")):
    generate_genome_index()

# Align the mRNA sequence
align_mrna_to_dna()
