def neighbor (list_, d):
    list_b = []
    for genome in list_:
        for j,e in enumerate(genome):
            for nu in ['A', 'T', 'C', 'G']:
                genome_b = genome
                if e!=nu:
                    genome_b = genome_b[:j] + nu + genome_b[j+1:]
                    # genome_b[j] = nu
                    list_b.append(genome_b)
    return list(set(list_b))


def neighbor_again (a_list ,d):
    for i in range(d):
        a_list += neighbor(a_list, d)
    return list(set(a_list))
    
if __name__ == "__main__":
    genome = input("Genome: ")
    d = int(input("d: "))


    b = neighbor_again([genome], d)

    print(len(b))
    for i in b:
        print(i)