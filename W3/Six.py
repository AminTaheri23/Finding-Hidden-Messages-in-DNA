import sys

from numpy.lib.function_base import sort_complex

sys.path.append('W2')

from Five_one import ProfileMostProbableK_mer
import numpy as np
from W2_4_1 import hamming_d

def FormTheMatrix (Dna_l):
    """Generates a profile matrix for given list of dna. The matrix consists of count of each nucleotide in every string. The first element of 2D list is counts of "A" nucleotide then, "C","G","T"

    Args:
        Dna_l (list): list of dna(s)

    Returns:
        list: 2D list of profile matrix
    """    
    # matrix = [ [0] for _ in range(len(Dna_l[0]))]
    n = len(Dna_l[0])
    matrix = np.zeros((4,n))
    bp = ['A', 'C', 'G', 'T']
    for i in range(len(Dna_l)):
        for j in range(n):
            matrix[bp.index(Dna_l[i][j])][j] += 1
    
    matrix+=1
    matrix/= len(Dna_l) + 4
    return matrix


def Score(motif_l):
    if motif_l == []:
        return 999
    b = []
    s = 0
    for j in motif_l:
        for i in motif_l:
            s+=hamming_d(j,i)
        b.append(s)
        s=0
    return min(b)

def GreedyMotifSearchPseudoCount(Dna, k, t):
    """Input: Integers k and t, followed by a collection of strings Dna. Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

    Args:
        Dna (list): list of dna strings
        k (integer): k as in k-mer (length of the pattern)
        t (integer): number of iteration

    Returns:
        List: list of most probable motifs 
    """    
    # BestMotifs = # motif matrix formed by first k-mers in each string from Dna
    
    first_k_mer_of_each_dna = []
    for s in range(len(Dna)):
        first_k_mer_of_each_dna.append(Dna[s][0:k])
    
    BestMotifs = first_k_mer_of_each_dna
    for i in range(len(Dna[0])-k+1): # k-mer selector
        motif= []
        motif.append(Dna[0][i:i+k])
        for j in range (1,t):
            profile = FormTheMatrix(motif)
            motif.append(ProfileMostProbableK_mer(Dna[j], k, profile))
        if Score(motif) < Score(BestMotifs): # we want to minimize the score (hamming_d)
                BestMotifs = motif
                
                
    return (BestMotifs)

if __name__ == "__main__":
    li = GreedyMotifSearchPseudoCount("""GCGCACCGAACCTCAGTGCAGTTCATGTATTTCGTCTGTCTCCCCAGCTGAACGAAAGGCAATGGTCAATTTCTGTTGTTATCAATAGCTCCCGAAATTGCTTACGCTCGGGTAAGCAGGGTTATTGGCAGAATACGTCGTCTTATGGATTACTAG
GTACGCGGACGCCGCGACCTGAGAGAGTTTGAAACGACGGACCTTAGAGACACTGGCAGATGGTAAGACCAAGGTTTTCCAGAAACCTTCCACAAGCCAAATGAAGAGACGCTACACAAGTGTGGTTGCATTACGTTGTCAATTTATTGTACCGCA
ACACCTCTTCCCCGCCATCGCAGGCCTCGAGACAGAATTCTTGATCCGCGTCTCACGCCATAGGAGAACGGCGTGAGTGGCAGTGCTTGGTAGAGTACTTGGGAAAAGTCAATGGACAGGGTTCTGAAGGAAGGCGAGAAAACACTTGACTGCAAG
AGTGGCAGCGAGCGCCTAAGACATGCTTTTCGGCCTGATTGCTCAGTCCAGCGAATAGTTAGTTTGCACTCCTGTCGGTGGATGTAGTAGCAACTGCAGATTGGAAGCTTTAACATGAGAGTGAGTGGCAGGAGTGAATTACAAACCATCGTCTGA
GAGCACATCGGGGAAACCCTTCGGGGTAATGGCAGTGGGCGCACTCTTTGACATGTGGGCGCGGTCTCGTCGGAGCGACGCTCCTAACACAGAACTGAGCATCGGCTCGGCTGGGCATGCAAGGGTGCGTAAGCTTAAGCCAAGAGGTTTGGCCAG
GGGTGTGACTTAACCTGTTTCACCGAAGAACATCGTTGGGTATTCTTCGCGCTATACGGCTCTCTTCGCCGGTTTTGTGAAAAGGCTAACAGGCAATGGCTGTGTATAGAATTCACGCTCCGTATATTTACGGTAACTGGCAGTAGACTTTCGCAG
ATCCTGGGACCACGTGATTATATGAGTTAACGCTCGGCGACTGGCAGAGGCGGAGGGTCTGAGGTTGTCTATCAATGTTATCAAGAGAAGGATGCTAGAGGGGTTGACCTAGCACCCCCACACCGACATGTGGTTAGACGAGTCTCTAGGGGGGGA
TTTAACTCCGCTCCGTATGAGACAAAAAAGGTCCTTGACAATGGTGAATCGTCCTAATTAGTTGGGTTGATAGTACTAGTTCAAGGGCCCACAAACGTAGTTTGATATATAGTCGTCTGACACTGGATCAGAGATAGTGGCAGGAAATACCCGCGG
CTGCAAGAGACGTGAACTTACGACCCGAACTTATTGGTGGCAGCCAAGTCTCTTGCGTATAGTAACTTCAACATTTGAAATCCACGTTTATGCGCTTTCTCCCCCGAGTCCCAACCATATGGCACTGTTTTGGTAATTGGCAGGGACTTCAGAGTT
TAAGTTTCAAGTGAGTTGTAATTTTAGCCAAATCCCACGCCCTAACGCATTAAAGATGCTCTCTGTCTTGGTCAAAAAGATTTAGCCATGATGTCCACGCATGCTGCGGAGAATGCCGTGCTTACAATATCCGCCAATGGCAGTATCCACGTATCC
CTCGGACCTTTGCACTCATATGGGGATTATGGACCATACGTCTTGACACTGGCCCTTATGTTGTCACTGTAAAGAAAGAATCTCGCCTGGCAATATGCCTGGCAACCTTGCTGGGAGGATAAATCGTCGCGTGCTACTGGCAGACTTCCGACCAAA
GCCCGTGCTATTCGCCAAGTACGTGCTAGTGGCAGGGTTTATCGAACCGACCGTTCGGGACAGGAATATGAGTACAATCGCATTCAGGGCTCTCACAGAACTCATCGAAAAGTTCAGTTGAAACTGTTTTTCGTAATACCCTTCCATATTTGGCAA
CCGATGGCCCCTTAGTCACCGGCCGCCTCCTTTACTCGAAGGACGGGAAGGCTCGGACGACCTCCAGTGAGGCAGCGGATAGTAGCTAGTGGCAGGTCGAAGGCGGCGTACACTGGAACCAGTACGGAAGTTGAGCATTGATCCGCAGCGATGATA
GCAAATGGCAGTCAGCTAACTGATATAAATACTGCGTGTCCAAGAGCGCGGAACTAGTCTGTGTAGCCGGGGGAGGTGGCCGAAATGAGGTTTCGATTAATGATACTTACGTTCTGAAGCACTTCCGTTCCGCCTTAGCTCCCGGGGAGGCTACGC
AATCGAAGCCATGTAGCGCTGTCGGCGAGCGATATAGTAAATGGCAGTAGTTCGGTGTTAATACTACTTAGCTGGAGTGTCGCCGACGTTGATCGCGCTAGGACGGCGTCTGGCAACGGGCAAAATCGTGCTTGCATAAGACAAGCTTGCGTCCCT
GAACAAGCAGGCACCGTAGAGATTACCTTGTGTTATTGACACCTTTGCTTGGGCTTCGCAGCGCCTGAAGTCATCCTGTGGCTGCTAACACTGGCTAGGTTCTGTCATTCAGCCTTGCGAGTTAATGGCAGCTAAATTCTATTATAGATTCTGAGG
GAAGACAACCTTGAGACGAATATGCATTCTAATATAGGCCCATGGTCAGAGACTGGCAGCCCCAATTCCGCCGTGCGGTAATGATCTTCCTGCGATTAGCTACATACCAATGGCCGTAGCCGGCCATAGCACCAGGGGACTAGACGTTCGAAGCAG
TTACTAGTTTTGAGCGTTGGAGCAGAAACCAAGGTGATAGTGTTGTTCGCAGACTCCGGCGAAGATCAAACGATGCTGTTTAAGGTAGCGTAATAAGTCTATTCTAAAGTGAATGGCAGGCTAGGTAAATTCGTCACCCTCTTTTCGTTTGGGTCT
ACAATATTTGCAAACGTATTCTACTATGTCGGAAGGTCGGCCCCGAGTGTAAGTGGCAGGGAGCCATGACCGAAGTGGCATCGTCTCAAGTTGTTTCGCTAGTTGGTGTTGGGCGTCCGGCCCGCGTTAGGAATGTTCCAGGTACACCGAAATATT
TGCTGGCGGGGCTTGCCACGCTGCGGCGATACATATGCTGGCCAGGCACTTAGCCACTGGTATAAAGTTTCGGGCACTGGCAGCCTTATGCAATGGGGTCTCACCGAGACCACGAGTGCCAATGTGCTTCTTCCGCTCGGGAGTTCCACCGTATCT
TGTCTAAAAATAATCGATGTCCAGTTCTTTTCCTGTAAGGCATTCACTCACCGTCTGATTTCTTTGATCTCCTATGCAGCCTCGGGGATGTATGACAAGGAGATCTGCGATAGCGCGCAGGGCAATGGCAGGTAGGACGATGACGAGCCGCTTGCC
TTGCCTTCTGGATGTCTACAGTATTCTCCGAGACCCTGCGCATTGAAGTTCGTGTGGCTTGCTAGTGGCAGTGCGGGGGGAGCTCTCCACGAATGGCCCATTGCCGGTGGTCCTGAGGCTAGCGCCATAGACTTAGATAACTCGTACCGTTTCGAC
GTAAATGGCAGATCCCCTCGTAAACTGAAGGCGCGACTATATCAAGCGGCTACGCCAGCAGCCTGTCACGTTCCCGGGTACTTATGACATATCTATTGGAGATGGCTATCGAGTCCAGTGATAGATCCTGCGCATCCCTCTGCTGAAAACGAGCGT
CTTGTCTTGTGTCTGACGAGTCAGCAAAACTGAGTTGACAGTGGCAGCTGGCGTTATGATGTTCCCAGGCACCACTCGGGTTCCAAGTACTGGTGAGAGCAGACATAGCGCACGAGAGCAGCACTATGCCATGTCATACTCTAGGTCTGGGAGCAT
GACCTCAGGTGTGCGGTCGTAGGGTTGGATAGTCTGGCGACTGGCAGCGGTCAAAACGACAGGCGAATTGGGTCTTATTCTCTACCGTAGAGCCTAGACAAGATCTAAGCACAGGGCCCAGAGCTTCAGCAGTCAACCCACGTGATTATCGTACAC""".split(sep="\n"),12,25)
    # filename = "dataset_159_5 (5).txt"
    # with open(filename, "r") as dataset:
    #     DNA = []
    #     for line in dataset:
    #         DNA.append(line.strip())
    # li = GreedyMotifSearch(DNA,12,25)
    for i in li:
        print(i)
#     truth = """TTC
# ATC
# TTC
# ATC
# TTC""".split().sort()
#     print(li.sort() == truth)