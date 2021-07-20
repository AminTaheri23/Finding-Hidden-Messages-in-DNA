import sys
sys.path.append('W2')

from W2_4_1 import hamming_d

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    """d(Pattern, Dna) = ∑ti=1 d(Pattern, Dna_i), the sum of distances between Pattern and each string in Dna = {Dna_1, ..., Dna_t}.
    Args:
        Pattern (string): the pattern :|
        Dna (list): list of strings 

    Returns:
        integer: sum of Hamming distance between the pattern and all of the dna  
    """    
    k = len(Pattern)
    distance = 0
    for text in Dna:
        Hamming_dis = 99999
        # pattern_prime = neighbor_again(Pattern)
        for i in range(len(text)-k+1):
            temp = hamming_d(text[i:i+k], Pattern)
            if Hamming_dis > temp:
                Hamming_dis = temp
        distance += Hamming_dis
    return distance

if __name__ == "__main__":
    # myfile = open("W3/dataset_5164_1 (3).txt", "r")
    # myline = myfile.readline()
    # a = myline
    # b = []
    # while myline:
    #     myline = myfile.readline()
    #     b.append(myline)
    # myfile.close()  
    
    with open("W3/dataset_5164_1 (4).txt") as inp:
        input_items = inp.read().strip().splitlines()
        pattern = input_items[0].strip()
        dna_sequences = input_items[1].strip().split()

    print(DistanceBetweenPatternAndStrings(pattern, dna_sequences))