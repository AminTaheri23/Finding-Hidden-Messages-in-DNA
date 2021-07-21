import sys
sys.path.append('W3')
sys.path.append('W4')

from Six import FormTheMatrix
from random import choices, randint, seed
from One import Score 

def Profile_Probability_K_mer(Text, k, prof):
    """Given a profile matrix Profile, we calculate the probability of every k-mer in a string Text and return it. 

    Args:
        Text (string): the DNA
        k (integer): as in k-mer
        prof (2D list): profile matrix of probability distribution

    Returns:
        list:  All probabilities of all k-mers
    """
    k_mer_probabilities = []
    k_mers = []
    for i in range(len(Text)-k+1):
        probability = 1.0
        for j, nucleotide in enumerate(Text[i:i+k]):
            for b, nuc in enumerate('ACGT'):
                if nucleotide == nuc:
                    probability *= prof[b][j]
        k_mer_probabilities.append(probability)
        k_mers.append(Text[i:i+k])
    return k_mers, k_mer_probabilities


def Profile_randomly_generated(Text, Profile, k):
    k_mer, k_mer_probabilities = Profile_Probability_K_mer(Text, k, Profile)
    return choices(population=k_mer, weights=k_mer_probabilities)[0]


def GibbsSampler(Dna: list, k: int, t: int, N: int):
    """GibbsSampler is a more cautious iterative algorithm that discards a single k-mer from the current set of motifs at each iteration and decides to either keep it or replace it with a new one. This algorithm thus moves with more caution in the space of all motifs,

    Args:
        Dna (list): List of DNA strings
        k (integer): As in k-mer
        t (integer): The number of iterations
        N (integer): Idk

    Returns:
        list: List of strings of best motifs that the algorithm find in the list of DNA strings
    """
    motif = []
    for s in range(len(Dna)):  # Select random k-mer from all DNA and append them to motif
        rnd = randint(0, len(Dna[0])-k)
        motif.append(Dna[s][rnd:rnd+k])

    BestMotifs = motif[:]

    for j in range(1, N):
        i = randint(0, t-1)
        # backup_motif = motif[:]
        motif.pop(i)
        profile = FormTheMatrix(motif)
        motif.insert(i, Profile_randomly_generated(Dna[i], profile, k))
        
        if Score(motif) < Score(BestMotifs):
            # print ("motif:      ", motif)
            # print ("Best motif: ", BestMotifs)
            print ("Score: ", Score(motif))
            if Score(motif)<65:
                for l in motif:
                    print(l)
            # accuracy(motif,truth)
            BestMotifs = motif[:]
            

    return BestMotifs

def accuracy (y_pred, y):
    Nominator = len(set(y_pred) & set(y))
    Denominator = float(len(set(y_pred) | set(y)))
    res = (Nominator/Denominator)*100
    print("Percent: ",res)


truth = """TCTCGGGG
CCAAGGTG
TACAGGCG
TTCAGGTG
TCCACGTG""".split(sep="\n")

if __name__ == "__main__":
    dna = """GCATGGGTTCACTCCATCTTTAGCCCTGGGTGTTAACAGAGGTGCAGAAACCCTCAAACTAATACGCGGAATGAGGAGACCAAATAGGGAGGAAATAGTGGTAACTAGCTTAGAGAAACGACACTAGGGATCAGTGTAATGATCTCAACATCTGTGGCATATGCGGTACTCACTTGGTGACCCGAATAACGGCCAACGGAATCGGAACGCATACGTTTCGGCAACGGGTGGATCTCCCAATCCGGGATTAGGTTTAACGGGTAGAACGTGCTGCAACACTAAAGAAAAACCAGCCTGTACTGGCATGGGTTCACTCC
ATCTTTAGCCCTGGGTGTTAACAGAGGTGCAGAAACCCTCAAACTAATACGCGGAATGAGGAGACCAAATAGGGAGGAAATAGTGGTAACTAGCTTAGAGAAACGACACTAGGGATCAGTGTAATGATCTCAACATCTGTGGCATATGCGGTACTCACTTGGTGACCCGAATAACGGCCAACGGAATCGGAACGCATACGTTTCGGCAACGGGTGGATCTCCCAATCCGGGATTAGGTTTAACGGGTAGAACGTGCTGCAACACTCCTGTCGATTTTCACAAAGAAAAACCAGCCTGTACTGGCATGGGTTCACTCC
CAGGTAACGACTAGCCTCTTTCCGGAAAGCCATAGCAGAAATTTACATAGCAGCGGCCCAGGCCCTCTAGCAAAATAACTTTGGGCCATGGCGAAGACATTGAAGCCGACTATGATTATTTACGCGAATCCATACTCTCCAAATAGCCGAGGGATTTTCACCCCATCGAATTCGATACGGGGCTTATAAGATAAGTACTATGTATGGACAATCACGTAGACTGGTATGGACGGGGGGTGGTCCGCCGGCGGGTTGGTAGTTCTTACATCTGGACGCTAGAACATAGGCCACGCGGACGTTATGGCCCGAAGCAATGT
GCAGTGCCGATCCACGTGAGAGGTCCCGCTACAAGTACAAGGCAGGTGAGCTGTAGAGCTTTGAAGGCTCAGTTTCTGCGGCTAGACATAGTGCGCGAGGTACTACACAGCTGTTGCGCGAACGGTTAGCCTTCAGAGCTTAAGATTTGAGCCCACCCCACGCAGTTAACTCGCAGTGTCCACTGGCTGTTGAATAAAACTATTTTCTCCGTGTTCACAATTACCTCGCCATTTTCACCGTGATCTGAGGTCTCTGATAATTTCGTGAGTCCACAGTGCCGTATCGATTATTTGGAACATCATTCTTTAAGAGAGTA
AATTGACACAGTACGGTTGCGGTGTTTTCGGAACGACTCTGACTGGAATCTGATGTAGCGTTGCACCAAAATAATTTCGGTACTGAGTTCAGGTTCTATTGGATGGGTGACACAAGTTCGACTGAATTTCATCTTGCAGACCCAATAATAAGACGTGTCTTACGGTACGAGACCTTGAGATTTTCACGTGTCCACGTTTGACCGCTTAACGTTGGGTACGCATTACGTCTCTCGTACAAAATTTCCTAGGCTTTTTCCCTCGCGTTTGGTGCGCCCTGACGGCACTCTGGAGACCCGCTCGCTTAGTTGAACATGAC
CCATTATAATTGTTGTCGCGGTCTCTGAGAAATGCACGTGCGGTCACCTACGGACCGGACTTCGCAACAATTGCCTAGTGAGCCGGCCATCTTGTGTCACAAAATAGAAGTATCCAAGCTAGTTAGCTTAGATTGGGGTTCTCAGGGTCAAACCTTGAGTTTTCGAGCTCAATTATTGTCTCACCCGATCATCACCAACGGTCACGGGAGGCTAGGAAGAGAAGCCCTCCGGATTGCTACCTCTTCAGCGGTTGCCGCGGTACGCAGGGTTGAGCTATCAACCGATAGACCCAGAACTTTAATTGTTCACCTCATGA
TTTTGAGCGACCCTACGCGGATTCTACCTCACCACCTTCGTCCGTTCTAGGCCTCCGGGCATTCACCCTGCCCCCAATGCAGTACAGTTCCTAGGCACCACTGAAAATGTATTGCAATGCAGGTTCATTCTAGGTACTCCAGGCTGGAACACAATCGTGCATAAACAGTGTAGAATACGTAGGCTAGCGTACAAGAGCCTTCCACACCTGGATTTGCTTAACTATAACATTAGGACCTAACTCAGCTGGAGTATGATAGCCGGCCTATATTGTACGATGACACGTACCGCGACTTGTTCACTTGACAACCGACCGTT
AGGATTCTTTTCGAATCGGTTAACGCGACGACGTGTAATATGCCTCAATACAATTTCGCAGCTTCAAGCCTAGAGACCGTAACTTGGAAAGGGGTGGTCGAGAAGACGTGCGCGTAAAGGAGCTCTGCGACTCGTCATTTAGCACACTGTGGGCAAAGTTTGCCAAATCCTTTCATGAGGGATATCGCAACTTCCAGCCCTTTAATTCTGCAGGGGTGACCCGTCACATTCAATGGGCATAAAACTTTAATTCACAGCAAAAATCCATGGCGCATTTACCTAAGGTCCATCCTCCGGATTTTGGGCGTCTTTAGAAC
CAAGGAAGAGGATTAAGCATGCGGGTGAGCTGAAATGAGCGATAAGGCTCCGGATTTTCTAGATAGGGGGGATCCAGAAGCAGCGTGGCTAGGGCTTCGGGAAGCGTGTCTTTCATCGATCGTCCCTGAGCTACGGTATCGTGCGGGGAAGGAGTGTTGAACGGCCCCGCGCTAGTCCAGCTTCACGAGGTAGTAAGTTTATGTATTTACACCTCGACCGGCCAACGAACATGTCCATTACCTTATAAGTTTGTTAAACATTTTGTGGTATATACCCTCGGATTCTTGAGCCGCCGACTCCGTTATTGCCATAATTA
ATGTTTAAGCTCAGATCTCTAGTGCCTCAAAATTTTCACTCCGTGAGTTTTGAAAGCTTTCCACATTGCATGTCCTGCCGTTCGTCTGAGGTGGCCTCATCAGTAGCCGGGCCAAGTGGCTAAGCGAATCACTCCAAGTGCACGTCACTCCGGTTCACGTATATAGGGGCCGGTCCGTATGCCCCAGTTAGCTGTATGGAAAAAGGCGCAAACACTAGTTGCGACCGCAAACATTGTACCTTGAAACGATAGACCGACGATTATGATGTAATCTTTGAAGCTACAAACCAATCTCACGTGCCTAACGTAAGTTTTAC
TTCCTGCCTATGAGCATGTACTGTAATATCCGTCCCATGACTACTCGAAAACCTCCGGATTTGATCATGGGGTGTAGGCCTTTACTTAAAACCAGATTACGCTCTAGATTACCTTAACCTAGCGCTACTCTCCTAAATATCCCTGCTCACGCGGGTTACCAACTCAGAATCTGTGTCCTGGCAGTTTATATGGGTCGCTGTTCTAAAGCAGTTAGGAGTGTAGCAGTGTGGCGTTCTCCGACCGTTCATATCTCTCGCGCTAGAGGAGTATGATGATCCCTTCCTCTGGCTCGACCAGAGAGATGACCCTATTATAG
AACTGGTGGAGCCCTTTGGAAGTGTCTCACGGCTTAGCGGCTTGGAGAACCATTGTCAAGTGTGCACCATTCAATTCGGCACTATGCTGAACAACCCAGCCGTATAGATTCTATATCTAAGCAAGCGGGCAGGAGCAGCTCTGTGGCTTACCTACGTACTTGCCGCCTAATTGGCCACTATGGGGCAACGGTTCACGATACGCGTGATCTGATACCCCTTAAACTGTACTTCGTGCTCACTCGGATTTTCACGTCTACTATTATATCCATTTAGACGTACCGCCCGAGAACTACCCGTTTACTAGAAAACCAAATGA
AGGAGGAGTCATTGACCAGTGCGCCTCCTATCTTATGATCCTTGTGTAACCAATAGGGGGATATAGGGACCAAGGTAAATAATATCACGCCTTTGGGAGGGTCGTTATACTCCACCGCACGCTTCAGATGGTCTCGGAAAACCATTTTCGATCAGGCCCGCATATCTCCGGAAGTTAACATGTTCAATACGGTCTTTCCTCCGTGCTTTCACGATTCACGTGTGGCCGACCGTCGGCCTCGACAATGCAGGATAGTTGGCTGTCCATCCTACCTGAGGGAAACGAAGATGTCGTTTGTGGCCGTAAGGCTCCTGGTT
ACCTGGACAAAGCGATAGCGATCTCCCACGCCCATGGTAGAGTTGTTATGCCAACGGCTTCTCAAACGCTATCTGCAAGCCCCCTAAGCGCGTACGGACGGTCAATTTAACATATTAACTATAGTTTAGCGTACCCTATCCCGCTTTGCTTGCACAGGGTGGAATTTGGCCGGTAGACCTCCGACCTTGTTGCTTGGGCTATGGGCTTGCGCCTTAGTTATTGACTTTCCTCCAAGTTTTCACGTGTGTATTACTCGACATTCAATTAGGTAAATATGGAGAAAGAGTCGCTCGCCTAAGGCCGGCTTCCTCGATGC
TGACCGGCCATAAAAAGTCCTACTATTGATTACCCCACTAGAGGGTTGCCTGGTAGGAATCACACTATCTATCGCAGCGGTGACTAAACATTGCCCTAATGACTTCCGATCGAAAAGCACATCTCCCCCGCACTGGACTCTCAAGCAACGCCACTTACCTCCGGACCATCACACGTACTGCGACTCGTTTCCCAACATATGATGACGGGAATCAGCGTCGGTGAACACATGCAGAACCTAAGACCCCAGGTAATAAGAGGGTAATACTTGCCTCAGGATTCTTGGTAAGTGGGACGCCGGCCGCCCTCTTATTAACA
CATCAGTTGTCCAGTAGTACTTCCTCTAAATAAATCACTTGCAACCCACCATCAACGTGCCAAAGCATAAACCCGGATTTTCACTGCATACATTATTCTCGCAAGCCCTTAAGTTTACATGAGTGGAAGTAATATGCTGGATGTGGGGATTCGAATACTTCCGGCGTTTTAATCCGCCAAACAGGTTAAAATATATGATACCCCTCAACGGACGTGAGAAATTTCCTGTGCAGACAATCGAGAGTAGTGCAGATTTTAGGCCTTACATAACAGTCACCCGTTTTCCTGAAAACTACGTTGGCGCTCTGCATTCACGT
ATGAGGAGCACCAATACCACGAACTGCGACACCAGTGTTCGGTGGACAGCTAAACTTCCAAGCCAGTTCCAACTGCTCGGTAAATCATTCCGGATTTTCAACCGGGTGGCGCCGCGTAGCACCACCTGACGATTCCCAGGTTAACGTAACCGGCTCCGCACAGTAGCCAGGAACCAAACGCAGTCCTTGAGCAGCTATTATTCTGTTCGCAATGAGTGGACTTAGCCGTTGCATCTTTTCACAGCACTGTCGAATGCACTGGTATACGACACCTGCTACCTTGCTCCTTTGCTCCTGAAGCAAGTAATGTAAACAAA
CGATATTAAGGCGAATGGGACTAGTACGGATTCAAGCAGTAACTTAACAACATTAGCGAATTCGTGAGGTTGAACTTCGTAAGATGTCTTCATCCCAGAACCCGGCCCGTCCGACCCGTTCTGTATAGGAGTCCGCCACGCCTGAATTACCGATGTAATATGGCACACCCACAAGTGTGGTGAAGTAGAGGGACGTTTCTTAAAGCCCTGTCGATCTGGCGCGTACATCTGGTGTTGTCACGATGCGAGCCAGTGTCAAGTCGCCGAACCAAGTCTAGCTCCCAGTCGTGACCTCCAATTCCTCCCTTTTTTCACCT
GTCGATAAAATAGATAACCAGTTCACGTAAGATGGCAGTTAACTCCCAGAGTATCTGTCCAGTTGCACTGCGCAAGTTCTGCCATGCGCCCTACACGGTGGTACCTAGCGCTGGTTTTCGCGTTCACCATTAGAACGGCTGTATTTTTTGCGATAGGCTGCCAGCGTTTGTTCTCTTTCCGGATTGGGATCGCCCCTCCCCACGGAGCCTAACACCAGTGAGCGAGCCTTGACGCCTATACTTACTACACAACATTCCGCTAGCAACTAGTCGTTTGCGCCTCAAGGCAGATAACCCCTCCGGATCAGCACATCACT
CTTATACATGGCAGGATATCTTTTCAAATAAGTCCTGTGGGGTGCGTGTGGATGCAATTGAAGTGGCGCGCAGTTTCAGTTCTGTGGGCACGACCCTCCGAGCTTTCACGTCGTTGGCAGCGGGTTTCAGTTGAGGCTAAACCGCGACTGCGAGTACTCGGGCGCGTGCATCTGATAAATTATCCGACTACCCCTATCATGTGCGAAACGGCCCGCCACGTGCGTGCGCTTAGACGTGATCGTGCACGGCTACAACTTCTTGATTTACTGCTGGCATGTCTAAAAAAATTCGAAGCTTGTGGAGCAGTCCCTAAGAA""".split(sep="\n")
    
    best = GibbsSampler(dna, k=15, t=20, N=2000)
    print("#### 0")
    seed(6985)
    for iteration in range(1, 20):
        candid =  GibbsSampler(dna, k=15, t=20, N=2000)
        print(f"#### {iteration}")
        if Score(candid) < Score(best):
            best = candid[:]
            print("\nSwitch\n")
        if Score(best)<66:
            for l in best:
                print(l)
            # accuracy(best,truth)
    
    
    best.sort()
    truth.sort()
    if best == truth:
        print(True)
    else:
        for l in best:
            print(l)
    
    # accuracy(best,truth)
    print(Score(best))
