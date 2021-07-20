def hamming_d (string1, string2):
    """Calculates the hamming distance of 2 strings. 
    for example:
        - hamming_d ("ACTT", "ACTT") = 0 
        - hamming_d ("ACTT", "ACTA") = 1
        - hamming_d ("ACTT", "ACAA") = 2

    Args:
        string1 (string): String that we want to calculate the hamming distance.  
        string2 (string): String that we want to calculate the hamming distance.  

    Returns:
        integer: The distance in integer
    """
    distance = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1

    return distance

if __name__ == "__main__":
    print(hamming_d("CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG", "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"))