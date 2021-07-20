text = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
k = 3

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

def FrequentWords(text, k):
    """
    This function will count the frequent K-mers in a text given, and the return the patterns that are most frequent.

    Args:
        text ([string]): [The text we are going to find the patterns in]
        k ([type]): [the k in k-mers. i.e. how long are the patterns. for example for k=3, we only count the patterns of length 3]
    Returns:
        list: list of most frequent k-mers
    """

    dic = {} # dictionary of empty. We will add patterns as the key and frequency of the patterns as the values
    max_count = 0 # Max freq of patterns
    for i in range(len(text) - k):
        proposed_pattern = text[i:i+k]
        count = pattern_count(text, proposed_pattern)
        if count>max_count:
            max_count = count

        dic[proposed_pattern] = count

    return [k for k,v in dic.items() if int(v) == max_count] 

string = ""
results = FrequentWords(text, k)

for pat in results:
    string += pat + " "

print(string)