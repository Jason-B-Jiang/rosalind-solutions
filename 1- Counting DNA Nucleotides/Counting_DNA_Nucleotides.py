def count_nucleotides(dna_file):
    with open(dna_file, 'r') as f:
        dna_string = f.readlines()[0].strip()
        nt_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

        for nt in dna_string:
            nt_count[nt] = nt_count[nt] + 1

        return " ".join([str(count) for count in [nt_count['A'], nt_count['C'], nt_count['G'], nt_count['T']]])


if __name__ == "__main__":
    print(count_nucleotides("rosalind_dna.txt"))
