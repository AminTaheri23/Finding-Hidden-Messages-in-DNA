def pattern_count(text, pattern):
    """This function will return the number of occurrences of a pattern in a string

    Args:
        text (string): The text that we want to find a pattern into
        pattern (string): The pattern

    Returns:
        int: The number of occurrences of the pattern in the text
    """
    count = 0
    for i in range(0, len(text) - len(pattern)+1):
        # print(text[i:i+len(pattern)])
        window = text[i:i+len(pattern)]
        if window == pattern:
            count += 1
    return count


def FrequentWords(text, k, t=0):
    """
    This function will count the frequent K-mers in a text given, and the return the patterns that are most frequent.

    Args:
        text (string): The text we are going to find the patterns in
        k (integer): the k in k-mer. i.e. how long are the patterns. for example for k=3, we only count the patterns of length 3
        t (integer): Threshold t. If a pattern occurs more than t times, we will add it to output.
    Returns:
        list: list of most frequent k-mer
    """

    dic = {}  # dictionary of empty. We will add patterns as the key and frequency of the patterns as the values
    # max_count = 0  # Max freq of patterns
    for i in range(len(text) - k):
        proposed_pattern = text[i:i+k]
        count = pattern_count(text, proposed_pattern)
        # if count > max_count:
        #     max_count = count
        dic[proposed_pattern] = count

    return [k for k, v in dic.items() if int(v) >= t]


def ClumpFinding(genome, k, L, t):
    """This function wil l patterns forming clumps in a string.

    Args:
        genome (string): The genome that we want to find clumps in
        k (integer): The k in the k-mer. How long should the patterns be. 
        L (integer): The length of the window we are striding in the genome
        t (integer): Frequency threshold of the occuring patterns. If the patter occurs more than t times, we will add it to the list of output.

    Returns:
        list: List of all patterns (k-mer) that we find repetitive in a small (L lengthen) region of the genome (occurrence more than t)
    """
    pattern = []
    ln_gn = len(genome)
    for i in range(ln_gn-L+1):
        window = genome[i:i+L]
        freq_list = FrequentWords(window, k, t)
        pattern += freq_list

    return list(set(pattern))


if __name__ == "__main__":
    with open("E_coli.txt") as f:
        genome = f.readline()
    # genome = input("Genome: ")
    k, L, t = map(int, input("k, L, t: ").split(sep=" "))
    results = ClumpFinding(genome, k, L, t)

    for pat in results:
        print(pat, end=" ")   

