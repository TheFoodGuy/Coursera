"""
David Liang 
Week 4 of coursera ucsd bme program
randomized algorithm
"""
from random import *
import Week3 as wk3

"""
dnas = list of dna, kmer = size of pattern, times = len(dnas)
"""
def randomized_motif_search(dnas, kmer, times):
    best_rand_motifs = list()
    for dna in dnas:
        rand_num = randint(0, len(dnas[0]) - kmer)
        best_rand_motifs.append(dna[rand_num:rand_num + kmer])
        # print(str(rand_num), str(dna))
    # print(best_rand_motifs)
    while True:
        motifs = list()
        cur_profile = wk3.pr(best_rand_motifs) #this part is messed up.
        # this is basically the motif(profile, dna) one.
        for cdna in dnas:
            motifs.append(wk3.most_profile_pat(cdna, kmer, cur_profile))
        # scoring might be wrong here
        # consensus_string = wk3.consensus1(cur_profile)
        if wk3.score(motifs) < wk3.score(best_rand_motifs):
            best_rand_motifs = motifs
        else:
            return best_rand_motifs

k_size = 8 
t_size = 5
dna_list = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
            "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
            "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
            "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
            "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
false_list = list()

while True:
    false_list = (randomized_motif_search(dna_list, k_size, t_size))
    best_score = wk3.score(dna_list)
    i = 0
    print(str(wk3.score(false_list)), str(wk3.score(dna_list)), i)
    if best_score > wk3.score(false_list):
        best_score = wk3.score(false_list)
        dna_list = false_list
        i = 0
    else:
        i += 1
    if i > 100:
        break
print(dna_list)


ans_list = ["TCTCGGGG",
            "CCAAGGTG",
            "TACAGGCG",
            "TTCAGGTG",
            "TCCACGTG"]
print(str(wk3.score(ans_list)))