def DNA_to_RNA(dna: str) -> str:
    return dna.replace('T', 'U')

if __name__ == "__main__":
    with open("rosalind_rna.txt", 'r') as f:
        dna_string = f.readlines()[0].strip()
        print(DNA_to_RNA(dna_string))