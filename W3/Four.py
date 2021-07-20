import sys
from typing import Pattern
sys.path.append('W2')
sys.path.append('W3')

from W2_7_1 import neighbor_again
from Seven import DistanceBetweenPatternAndStrings

def MedianString(Dna, k):
    """Input: An integer k, followed by a collection of strings Dna.
Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)
    Args:
        k (integer): k-mer
        Dna (list): list of strings 

    Returns:
        integer: median
    """    
    
    distance = 9999
    median = []
    ptrn = ""

    for i in range(k):
        ptrn += "A"
    
    Patterns = neighbor_again([ptrn], k)

    for Pattern in Patterns:
        temp = DistanceBetweenPatternAndStrings(Pattern, Dna)
        if distance > temp:
            distance = temp
            median = [Pattern]
        elif distance == temp:
            median.append(Pattern)

    return median

if __name__ == "__main__":
    
    # with open("W3/dataset_158_9 (3).txt") as inp:
    #     input_items = inp.read().strip().splitlines()
    #     k = input_items[0].strip()
    #     k = int(k)
    #     dna_sequences = input_items[1].strip().split()

    k = 7
    dna_sequences = """CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC
GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC
GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG""".split("\n")
    
    print(MedianString(dna_sequences, k))