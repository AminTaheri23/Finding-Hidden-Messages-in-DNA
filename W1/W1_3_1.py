dna_strand = "TTGTGTC"
dna_strand_r = ""

for nucleotide in dna_strand:
    if nucleotide == "A":
        dna_strand_r += "T"
    elif nucleotide == "T":
        dna_strand_r += "A"
    elif nucleotide == "G":
        dna_strand_r += "C"
    elif nucleotide == "C":
        dna_strand_r += "G"

f = open("w131.txt", "a")
f.write(dna_strand_r[::-1])
f.close()

