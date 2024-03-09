def to_rna(dna_strand):
    new_strand = ''
    for letter in dna_strand:
        if letter == 'G':
            new_strand += 'C'
        if letter == 'C':
            new_strand += 'G'
        if letter == 'T':
            new_strand += 'A'
        if letter == 'A':
            new_strand += 'U'
    return new_strand