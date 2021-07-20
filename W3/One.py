
import sys
sys.path.append('W2')

from W2_7_1 import neighbor_again

def MotifEnumeration(DNA, k, d):
    """This function will brute force through
     the all of the possibilities of
      motifs that are k-mer (k variable)
       and have at least d mismatches.

    Args:
        DNA (list): list of DNA strings that we want to find (k,d) motifs in
        k (integer): The k in k-mer
        d (integer): The distance between the original pattern and the mismatched one.
    Returns:
        list : list of all (k,d) motifs
    """
    pattern = []

    for String_of_dna in DNA:
        for i in range(len(String_of_dna)-k+1):
            all_neighbors = neighbor_again([String_of_dna[i:i+k]], d)
            for neigh in all_neighbors:
                f = 0
                for j in DNA:
                    for s in range(len(j)-k+1): 
                        nos = neighbor_again([j[s:s+k]],d)
                        if neigh in nos:
                            f+=1
                            if f == len(DNA): # Checks that we have this pattern in all of the DNA strings
                                pattern.append(neigh)
                                f=0
                            break
                    
    return list(set(pattern))

if __name__ == "__main__":
    k,d = map(int, (input("k, d: ").split()))
    print(type(k))
    print("DNA (use Ctrl+Z when you are done): ")
    input_str = sys.stdin.read()
    cleaned = input_str.split(sep="\n")[:-1]
    bib = MotifEnumeration(cleaned, k, d)

    for e in bib:
        print(e)