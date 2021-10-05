def my_hamming_dna(dna1, dna2):  # GGACTGA" && "GGACTGA
    i = 0
    count = 0
    if len(dna1) == len(dna2):
        while (i < len(dna1)):  #
            if dna1[i] != dna2[i]:
                count += 1
            i += 1
        return count
    else:
        return -1


print(my_hamming_dna('GGAbabA', 'GGACTGA'))
