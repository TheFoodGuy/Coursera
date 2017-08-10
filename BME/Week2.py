"""
David Liang
this is to call the week1 materials onto here if required
"""
import Week1 as wk1
"""
this is to find the number of mismatches of similar strings
"""
def hamming_distance(main_string, mis_string):
    count = 0
    for i in range(len(main_string)):
        if main_string[i] != mis_string[i]:
            count += 1
    return count

"""
this counts all approximate occurences of a pattern in a string
"""
def app_pattern_match(text, kmer, dup):
    count = list()
    text_len = len(text)
    pat_len = len(kmer)
    for index in range(text_len-pat_len+1):
        cur_pat = text[index:index+pat_len]
        mismatch = hamming_distance(cur_pat, kmer)
        if mismatch <= dup:
            count.append(index)
    return count

"""
this counts the number of times the pattern matches approximately
"""
def app_pattern_count(text, pattern, dup): 
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        new_pattern = text[i:len(pattern)+i]
        if hamming_distance(pattern, new_pattern) <= dup:
            count = count + 1
    return count
"""
this is to find the min and max points of GC areas 
"""
def shewSearch(genome):
    k = 0
    hold_num = {}
    for i, v in enumerate(genome):#enumerate adds a counter to each index of the letter
        hold_num[i] = k
        if v == 'G':
            k = k + 1
        elif v == 'C':
            k = k - 1
    #check to see if 11 and 24 have the lowest count
    min_count = min(hold_num.values())
    new_hold = set()
    for i in hold_num:
        if hold_num[i] == min_count:
            new_hold.add(i)
    return new_hold


"""
find the most frequent pattern with mismatches in a string
"""
def frequent_mistmatches(text, k, dup):
    freq_pat = set()
    close = [0 for i in range(4**k)]
    for i in range(0, len(text)-k):
        neighborhood = neighbors(text[i:k+i], dup)
        for pattern in neighborhood:
            index = wk1.PatternToNumber(pattern)
            close[index] = close[index] + 1
    max_count = max(close)
    for i in range(0, 4**k -1):
        if close[i] == max_count:
            pattern = wk1.NumberToPattern(i, k)
            freq_pat.add(pattern)
    return freq_pat

"""
just like frequent_mistmatchs but reverse
"""
def frequent_mistmatches_rev(text, k, dup):
    freq_pat = set()
    close = [0 for i in range(4**k)]
    for i in range(0, len(text)-k):
        neighborhood = neighbors(text[i:k+i], dup)
        #reverse complement here seems to work here as well
        for pattern in neighborhood:
            index = wk1.PatternToNumber(pattern)
            close[index] = close[index] + 1
    max_count = max(close)
    for i in range(0, 4**k -1):
        if close[i] == max_count:
            pattern = wk1.NumberToPattern(i, k)
            freq_pat.add(pattern)
    return freq_pat

"""
generate d-neighborhood neighbors, basically neighbors but with d = 1 
"""
def close_neighbors(pattern):
    neighborhood = set()
    for i in range(0, len(pattern)):
        symbol = list(pattern)[i]
        for nuc in ["A", "C", "G", "T"]:
            if symbol != nuc:
                temp_string = pattern[:i] + nuc + pattern[i+1:]
                neighborhood.add(temp_string)
    neighborhood.add(pattern)
    return neighborhood

"""
generate d-neighborhood neighbors
"""
def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:len(pattern)], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:len(pattern)], text) < d:
            for nuc in ['A', 'C', 'G', 'T']:
                neighborhood.add(nuc + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood
