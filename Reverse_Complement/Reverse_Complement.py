def complement_nt(nt: str) -> str:
    """Returns the complementary nucleotide for a given nucleotide, nt"""
    nt_mapping = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    return nt_mapping[nt]


def get_dna_reverse_complement(dna: str) -> str:
    """Return reverse complement strand for a given DNA sequence"""
    return "".join([complement_nt(nt) for nt in dna][::-1])


if __name__ == '__main__':
    with open("rosalind_revc.txt", "r") as f:
        dna_string = f.readlines()[0].strip()
        output = open("solution.txt", "w")
        output.write(get_dna_reverse_complement(dna_string))
        output.close()