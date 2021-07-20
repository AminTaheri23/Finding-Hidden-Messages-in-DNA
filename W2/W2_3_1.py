def min_skew(genome):
    """This function returns a list of minimum skew indexes of a genome.
     This is basically the difference between the G and C in the genome. 
     The skew formula in a nutshell is that we traverse the genome and 
     if we encounter a G we add 1 point to a diff variable, and if we 
     encounter a C we -1 point from the variable. 

    Args:
        genome (string): The whole genome. 

    Returns:
        list: list of indexes of the genome where the skewness is minimum.
    """

    skew_list = [0]
    min_skew_list = []
    min = 999999  # I am tired
    skew = 0

    for (i, e) in enumerate(genome):
        if e == "G":
            skew += 1
        if e == "C":
            skew += -1

        if skew == min: 
            min_skew_list.append(i+1)
        if skew < min and (e=="G" or e=="C"):
            min_skew_list = []
            min = skew
            min_skew_list.append(i+1)

        skew_list.append(skew)

    
    for sk in min_skew_list:
        print (sk, end=" ")
    
# if __name__ == "main":
genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
min_skew(genome)