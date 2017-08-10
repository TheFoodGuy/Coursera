"""
Using week1 and week2 toolkit
"""
import Week1 as wk1
import Week2 as wk2

"""
find all (k,d)-motifs in a collection of strings
"""
def motif_enumberation(Dnas, kmer, dup):
    motif_pat = set()
    counter = 0
    for dna in Dnas: #getting each dna string here
        c_list = set()
        for index in range(len(dna)-kmer+1):
            # getting each pattern by parsing positions
            neighbor_list = wk2.neighbors(dna[index:index+kmer], dup)
            neighbor_list.add(dna[index:index+kmer]) #adding the original pattern
            # now we gotta compare and see if they match in all of the list
            # so from the first line, if they don't match with the next few lines
            # remove them from the list
            for n_dna in neighbor_list:
                c_list.add(n_dna)
            c_list.add(dna[index:index+kmer])
        if counter == 0:
            motif_pat = c_list
            counter += 1
        motif_pat = motif_pat.intersection(c_list)
    return list(motif_pat)

"""
this will compare x number of dnas and pick the one with the least scoring
count(motif) = the number of nucleotides outside of the conversed
score(motif) = count(motif)
profile(motif) = percentage of nucleotides per position (adds to 1 in total)
consensus(motif) = most popular letters in each column of the motif matrix
"""
def score(dnas):
    # just using a dna string as the length to keep track of
    # print("not the actual error here", dnas)
    dict_list = list()
    score_value = 0
    for index in range(len(dnas[0])):
        nuc_dict = dict()
        for nuc in ['A', 'C', 'G', 'T']:
            nuc_dict[nuc] = 0
        for dna in dnas:
            for nuc in ['A', 'C', 'G', 'T']:
                if nuc == dna[index]:
                    nuc_dict[nuc] += 1
                    break
        dict_list.append(nuc_dict)
    for nuc_dict in dict_list:
        max_key = max(nuc_dict, key=nuc_dict.get)
        max_count = len(dnas) - nuc_dict[max_key]
        score_value = score_value + max_count
    return score_value

"""
this is to find the popular sequence here 
"""
def consensus(dnas):
    # just using a dna string as the length to keep track of
    dict_list = list()
    score_value = ""
    for index in range(len(dnas[0])):
        nuc_dict = dict()
        for nuc in ['A', 'C', 'G', 'T']:
            nuc_dict[nuc] = 0
        for dna in dnas:
            for nuc in ['A', 'C', 'G', 'T']:
                if nuc == dna[index]:
                    nuc_dict[nuc] += 1
                    break
        dict_list.append(nuc_dict)
    for nuc_dict in dict_list:
        max_key = max(nuc_dict, key=nuc_dict.get)
        score_value = score_value + max_key
    return score_value

""" 
creating a profile matrix - a test drive to see if i understand how to do it\
test-drive here
"""
def profile(dnas, kmer):
    times = len(dnas) # getthing the number of dna sequences in the list
    profile_matrix = dict()
    for nuc in ['A', 'C', 'G', 'T']: # this will hold the final values
        profile_matrix[nuc] = list()
    for index in range(0, kmer):
        nuc_dict = dict()
        for dna in dnas:
            base = dna[index]
            if base not in nuc_dict:
                nuc_dict[base] = 1
            else:
                nuc_dict[base] += 1
        # i should have the base column counted here
        for nuc in ['A', 'C', 'G', 'T']:
            if nuc not in nuc_dict or nuc_dict[nuc] == 0:
                profile_matrix[nuc].append(0)
            else:
                profile_matrix[nuc].append(nuc_dict[nuc]/float(times))
    return profile_matrix

"""
this effectively takes in a list of dnas and a kmer size pattern
then tries to find the least distance or the best pattern as such.
"""
def median_string(dnas, kmer):
    distance = 100000000
    median = ""
    for i in range(4**kmer - 1):
        pattern = wk1.NumberToPattern(i, kmer)
        current_distance = pat_distance_str(pattern, dnas)
        if distance > current_distance:
            distance = current_distance
            median = pattern
    return median
"""
a string pattern followed bt a collection of string dna
that produces the hammingdistance
"""
def pat_distance_str(pattern, dna):
    kmer = len(pattern)
    distance = 0
    for c_dna in dna:
        ham_dist = 1000000000
        for index in range(len(c_dna) - kmer + 1):
            kmer_pat = c_dna[index:index+kmer]
            if ham_dist > wk2.hamming_distance(pattern, kmer_pat):
                ham_dist = wk2.hamming_distance(pattern, kmer_pat)
        distance = distance + ham_dist
    return distance

"""
greedy motif searcher here which selects the most attractive alternative at 
each iteration. It finds the approximate solution.
basically, given a sequence text, with kmer size, and a profile matrix of the nucleotide
probabiliy, which pattern has the best?
"""
def most_profile_pat(text, kmer, profile):
    best_prob = 00
    best_sequence = text[:kmer]
    for index in range(len(text) - kmer + 1):
        pattern = text[index:index + kmer]
        # calculating the best probability here until the end
        cur_prob = 1
        for pos, nuc in enumerate(pattern):
            cur_prob *= profile[nuc][pos]
        if best_prob < cur_prob:
            best_prob = cur_prob
            best_sequence = pattern
    return best_sequence

"""
official greedy motif searcher here
Starts by forming a motif matrix from the first string and kmer. 
This builds a profile matrix from it and sets motif2 to the profile of dna2.
dnas = a list of dna
kmer = the size of pattern
times = the number of dnas in the list
http://www.mrgraeme.co.uk/greedy-motif-search/
"""
def greedy_motif(dnas, kmer):
    # creates motif matrix formed by first k-mers in each string
    best_motif = profile(dnas, kmer)
    best_list = list()
    # finding the score here 
    for dna in dnas: 
        pattern = dna[:kmer]
        best_list.append(pattern)
    best_score = score(best_list) # get the best score for the inital kmers
    # this part does the work of looking for the best motif set with the 
    # least score count.
    for index in range(len(dnas[0]) - kmer + 1):
        cur_motif = dnas[0][index:index+kmer]
        cur_motifs = list()
        cur_motifs.append(cur_motif)
        # this will create the best profile here.
        for cur_index in range(1, len(dnas)):
            #cur_profile = profile(cur_motifs, kmer)
            cur_profile = pr(cur_motifs)
            motif1 = most_profile_pat(dnas[cur_index], kmer, cur_profile)
            cur_motifs.append(motif1)

        if score(cur_motifs) < best_score:
            best_score = score(cur_motifs)
            best_list = cur_motifs

    return best_list

"""
this is to apply Laplace's rule of succession to greedy motif search 
which will improve the accuracy overall
Basically, this increases the total by len(dnas) * 2.
or, everything is added by 1.
"""
def pr(dnas):
    matrix_dict = {k: [1] *len(dnas[0]) for k in ['A', 'C', 'G', 'T']}
    for index in range(0, len(dnas[0])):
        for dna in dnas:
            # print(str(index), dna)
            base = dna[index]
            matrix_dict[base][index] += 1
    for nuc in ['A', 'C', 'G', 'T']:
        matrix_dict[nuc] = [x / float((len(dnas[0])*2)) for x in matrix_dict[nuc]]
    return matrix_dict

# k_size =3 
# t_size = 5
# dna_list = ["GGCGTTCAGGCA",
#             "AAGAATCAGTCA",
#             "CAAGGAGTTCGC",
#             "CACGTCAATCAC",
#             "CAATAATATTCG"]

# print("yeaaah", greedy_motif(dna_list, k_size))

# """ answers to this problem for lapace switch
# TTC
# ATC
# TTC
# ATC
# TTC
# """
# k_size = 12
# t_size = 25
# with open("test.txt", 'r') as f: 
#     dna_list = list()
#     for line in f:
#         dna_list.append(line.rstrip())
#     a = greedy_motif(dna_list, 12)
#     for i in a:
#         print i

# dna_list =    ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
#                 "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
#                 "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
# print(median_string(dna_list, 7))