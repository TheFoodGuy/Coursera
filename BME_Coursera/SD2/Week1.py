"""this is week1 of the second course for ucsd """
from random import shuffle
""" string composition problem
input: k-integer and a string text
output: composition(text)
"""
def composition(text, kmer):
    comp_list = list()
    for index in range(len(text) - kmer + 1):
        comp_list.append(text[index:index+kmer])
    return sorted(comp_list)

# with open("test.txt", 'r') as f:
#     input_file = f.readline()
#     a = composition(input_file, 100)
#     for i in a:
#         print(i)

""" string reconstruction problem
given a list of kmers, this will reassemble the dna sequence based off 
them.
i give up on this python thing, it's not stripping newline correctly
"""
def genome_path(kmers):
    a = kmers[0]
    for index, entry in enumerate(kmers):
        if index == 0:
            continue
        a = a + entry[-1]
    return a

# kmer_list = list()
# with open("input.txt", 'r') as readfile:
#     for line in readfile:
#         entry = line.strip()
#         kmer_list.append(entry)

# print(genome_path(kmer_list))

""" overlap graph problem
this construct the overlap graph of a collection of kmers 
Nodes are formed for each kmer by a directed edge if suffix and prefix match
"""
def overlap_graph(kmer_list):
    # overlap_matrix = [[0 for x in range(len(kmer_list))] for y in range(len(kmer_list))]
    for entry in kmer_list:
        for n_entry in kmer_list:
            if n_entry[:len(entry)-1] == entry[1:]:
                print("{} -> {}".format(entry, n_entry))
                break

""" De Bruijn Graph from string problem 
This takes in k-pattern size and a string text, then 
it produces an adjacency list 
"""
def de_bruijn(text, kmer_size):
    kmer_list = dict()
    kmers = list()
    for index in range(len(text)-kmer_size +1):
        kmer_list[text[index:index+kmer_size-1]] = list()
        kmers.append(text[index:index+kmer_size])
    # print("{}".format(len(kmer_list)))
    # print(kmer_list)
    # print(kmers)
    for kmer in kmers:
        kmer_list[kmer[:kmer_size-1]].append(kmer[1:])
    for key, value in kmer_list.items():
        print("{} -> {}".format(key, ", ".join(value)))
    return(kmer_list)

