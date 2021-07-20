from random import Random, choices,random
import sys
sys.path.append('W3')

from Six import FormTheMatrix
from Five_one import ProfileMostProbableK_mer

def GibbsSampler(Dna, k, t, N):
    motif = []
    for s in range(len(Dna)):
        rnd = random.randint(0,len(Dna[0])-k)
        motif.append(Dna[s][rnd:rnd+k])

    BestMotifs = motif[:]

    for j in range(1,N):
        i = random.randint(0,j)
        
    return BestMotifs
print(choices(population=['A','B','C'],weights=[0.1,0.3,0.4]))