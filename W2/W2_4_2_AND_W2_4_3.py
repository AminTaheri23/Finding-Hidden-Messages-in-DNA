from os import sep
from W2_4_1 import hamming_d
import pprint

def pattern_count_hamming_d(text, pattern, d):
    """This function will return the number of occurrences of a approximate 
    pattern(with <=d distance with the original pattern) in a string

    Args:
        text (string): The text that we want to find a pattern into
        pattern (string): The pattern
        d (integer): threshold for the hamming distance

    Returns:
        int: The number of occurrences of the pattern in the text
    """
    ls = ""
    for i in range(0, len(text) - len(pattern)+1):
        # print(text[i:i+len(pattern)])
        window = text[i:i+len(pattern)]
        if hamming_d(window, pattern) <= d:
            ls += str(i) + " "
    return ls[:-1]

list_mine = pattern_count_hamming_d("TACGCATTACAAAGCACA", "AA", 1)
print(len(list_mine.split()))