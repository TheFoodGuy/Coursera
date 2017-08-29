""" was being dumb, i thought it was randomized or something """
""" string reconstruction problem
given a list of kmers, this will reassemble the dna sequence based off 
them.
"""
def genome_path(kmer_list):
    # print(kmer_list)
    len_ans = len(kmer_list) + len(kmer_list) - 1
    sequence_ans = ""
    check_pattern = "" # this is for the first position
    # I think I would have to find the starting point before automating it
    for entry in kmer_list:
        counter = 0
        check_pattern = entry
        for nxt_entry in kmer_list:
            if check_pattern[:len(entry)-1] == nxt_entry[1:]:
                break
            else:
                counter += 1
        # this checks if the pattern actually gone through the entire list
        if counter == len(kmer_list):
            break
    sequence_ans = check_pattern
    abs_no_list = list() # this is for bad elements that will create a infinite loop
    abs_no_list.append(check_pattern)
    # temp_ans = sequence_ans
    counter = 1
    while True:
        check_counter = 1 # this is a flag to determine if the sequence_ans is stuck in a loop
        if len(sequence_ans) == len(kmer_list) + len(kmer_list[0])-1:
            break
        for entry in kmer_list:
            if entry in abs_no_list:
                continue
            # print("entry = {} sub_entry = {} sequence_ans = {} sub_sequence = {}".format(entry, entry[:len(entry)-1], sequence_ans, sequence_ans[counter:]))
            if entry[:len(entry)-1] == sequence_ans[counter:]:
                if entry not in abs_no_list:
                    sequence_ans = sequence_ans + entry[-1]
                    # ans.append(entry)
                    counter += 1
                    check_counter = 0
        # answer is bad here
        if check_counter == 1:
            sequence_ans = sequence_ans[:len(sequence_ans)-1]
            bad_element = sequence_ans[len(sequence_ans)-len(kmer_list)-1:]
            abs_no_list.append(bad_element) # inserting the bad element in
            counter -= 1
        # print("counter = {}, check_counter = {}".format(counter, check_counter))
    return sequence_ans