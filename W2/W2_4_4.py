from W2_7_1 import neighbor_again

def FrequentWordsWithMismatches(Text, k, d):
    """ It uses a single map that counts the number of times a given string has an approximate match in Text. For a given k-mer substring Pattern of Text, we need to increase 1 to the count of every k-mer that has Hamming distance at most d from Pattern.  The collection of all such k-mers is called the d-neighborhood of Pattern, denoted Neighbors(Pattern, d). 

    Args:
        Text (string): The string that we want to find the most frequent approximate patterns with at most d hamming distance in.
        k (integer): the k in the k-mer. patter length
        d (integer): hamming distance. the patterns can have at most d distance from the pattern that is in the text.
    Outputs:
        list: list of most frequent approx patterns.
    """    
    Patterns = ""
    freqMap = {}
    n = len(Text)

    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        neighborhood = neighbor_again([Pattern], d)

        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1  

    m = max(freqMap.values())
    for key in freqMap.keys():
        if freqMap[key] == m:
            Patterns += key + "\n"
    return Patterns

# if __name__ == "__main__":
print(FrequentWordsWithMismatches("", 7, 2))