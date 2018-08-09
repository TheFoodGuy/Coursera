import numpy as np
from copy import copy, deepcopy

BLOSUM62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 
'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2},
'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 
'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 
'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 
'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 
'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 
'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 
'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 
'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 
'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 
'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 
'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 
'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 
'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 
'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 
'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 
'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

PAM250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}# reading BLOSUM62.txt 
def readingBLO(filename='BLOSUM62.txt'): 
    matrix = dict()
    with open(filename, 'r') as f: 
        for line in f: 
            content = (line.strip('\n')).split()
            matrix[content[0]] = list(map(int,content[1:])) # converting to a list of int in python

def getVariable(var):
    return var

# global alignment
# INPUT: two protein strings written in the single-letter amino acid 
# OUTPUT: the maximum alignment score of these strings followed by an alignment
# USING BLOSUM62 for the scoring matrix and mismatches as well
"""
Doing this because I don't feel like coding dynamic programming right now 
This is a modified LCS in which we have to create '-' to create the best score value
based on the scoring matrix given which is used for matches or misses and what nots
    
    The scoring matrix has mismatches score just not indel penalty which is given
    green == deletions or vertical, blue == insertions or horizontal 
    red/purple or matches/mismatches == diagonal edges

INTPUT: 
PLEASANTLY
MEANLY

OUTPUT: 
8
PLEASANTLY
-MEA--N-LY

sigma == 5
"""
# remember that str1 is x and str2 is y in terms of matrix
def globalAlignment(str1='PLEASANTLY', str2='MEANLY', sigma=-5, matrix=BLOSUM62):
    # base case if there is nothing to compare 
    if len(str1) == 0 or len(str2) == 0: 
        return 0
    s1 = len(str1)
    s2 = len(str2)
    s11 = s1
    s22 = s2
    # incrementing all by one is due to the recurrence relation 
    # initializing everything to zeroes in case I gotta go -1 for i and/or j
    # to get a better picture of this: str2 is y and str1 is x
    alignmentScores = [[0 for j in range(s1+1)] for i in range(s2+1)]
    # this is setting the insertions and deletions 
    # Using the comment from stepik which makes sense to consider this option 
    for i in range(1, s2+1):
        # alignmentScores[i][0] = alignmentScores[i-1][0] + sigma 
        alignmentScores[i][0] = alignmentScores[i-1][0] + sigma 

    for j in range(1, s1+1):
        # alignmentScores[0][j] = alignmentScores[0][j-1] + sigma
        alignmentScores[0][j] = alignmentScores[0][j-1] + sigma
    
    for i in range(1, s2+1): 
        for j in range(1, s1+1): 
            # if str2[i-1] != str1[j-1]:

            # the first three reccurence relations here or if they are mismatches 
            # considering the scores of indel and mismatches 
            alignmentScores[i][j] = max(alignmentScores[i-1][j] + sigma,
                                        alignmentScores[i][j-1] + sigma, 
                                        alignmentScores[i-1][j-1] + BLOSUM62[str1[j-1]][str2[i-1]])
      
            # # if the string at each index is the same.
            # elif str2[i-1] == str1[j-1]: 
            #     alignmentScores[i][j] = alignmentScores[i-1][j-1] + BLOSUM62[str1[j-1]][str2[i-1]]

    # backward output sequence here 
    # the idea here is to move backwards from alignmentScores[s2][s1] to 0.
    # if it moves up == deletion of s2 to s1, left == insertion of s2 to s1, diagonal is mismatches or matches doesn't matter
    firstSequence = str1 # this is going to hold the values
    secondSequence = str2  
    sequenceScore = alignmentScores[s2][s1] 
    while s1 != 0 or s2 != 0:
        a = "{} {} {}".format(s2, s1, sequenceScore)
        # checking if there's a match so i can skip
        if ((sequenceScore) - BLOSUM62[str1[s1-1]][str2[s2-1]] == alignmentScores[s2-1][s1-1]):
            s1-=1
            s2-=1
            a = "1 " + a
        else:
            # how do I tell the difference between which sigma it is? 
            if ((sequenceScore) - sigma == alignmentScores[s2-1][s1]):
                s2-=1                
                firstSequence = firstSequence[:s1] + '-' + firstSequence[s1:]
                a = "2 " + a

            elif ((sequenceScore) - sigma == alignmentScores[s2][s1-1]):
                s1 -= 1
                secondSequence = secondSequence[:s2] + '-' + secondSequence[s2:]
                a = "3 " + a

            else: 
                s1-=1
                s2-=1
                a = "4 " + a
        # print(a)
        sequenceScore = alignmentScores[s2][s1]

    # prepending or appending the -, last check 
    firstSequence, secondSequence = applyIndel(firstSequence, secondSequence, len(str2) > len(str1))

    print(alignmentScores[s22][s11])
    # print(firstSequence)
    # print(secondSequence)
    printMatrix(str1, str2, alignmentScores)
    return alignmentScores[s22][s11], [firstSequence, secondSequence]

def applyIndel(str1, str2, status): 
    # that means str1 needs some mods if status == true
    a,b = len(str1), len(str2)
    
    if a != b and (str1[-1] != '-' or str2[-1] != '-') and str1[-1] != str2[-1]:
        if status == True:
            str1 = str1 + "-"
            a+=1
        else: 
            str2 = str2 + "-"
            b+=1
    status = b > a

    if a != b and (str1[0] != '-' or str2[0] != '-') and str2[0] != str1[0]:
        if status == True:
            str1 = "-" + str1
            a+= 1
        else: 
            str2 = "-" + str2
            b+=1 
    return str1, str2

# this is to print out the matrix or the scoring matrix to make it nicer to look at.
def printMatrix(str1, str2, alignment):
    print(np.matrix(alignment))

"""
    The Idea is the same as global alignment except this approach produces the best 
    conserved regions and their scores 
    How it works exactly I'm going to try and figure out later on
    
    Questions: TODO: DO I KNOW THE SIGMA VALUE? 
    Is it everytime there is a negative number into the alignment score, I should set it to 0? 

    Answer:
    From source to every other node, it is connected by a zero-weighted edge and connecting all these 
    nodes to sink by the same edge. 
        Reference: Kwat ME -> Imma have the option 0 in the step that computes the max to avoid reinventing

    # local alignment
    Sample Input:
        MEANLY
        PENALTY
    Sample Output:
        15
        EANL-Y
        ENALTY

"""
# local alignment
# with a minor modificaiton
def localAlignment(str1='MEANLY', str2='PENALTY', sigma=-5, matrix=PAM250):
    # base case if there is nothing to compare 
    if len(str1) == 0 or len(str2) == 0: 
        return 0
    s1 = len(str1)
    s2 = len(str2)
    s11 = s1
    s22 = s2

    alignmentScores = [[0 for j in range(s1+1)] for i in range(s2+1)]

    for i in range(1, s2+1):
        # alignmentScores[i][0] = alignmentScores[i-1][0] + sigma 
        alignmentScores[i][0] = alignmentScores[i-1][0] + sigma 

    for j in range(1, s1+1):
        # alignmentScores[0][j] = alignmentScores[0][j-1] + sigma
        alignmentScores[0][j] = alignmentScores[0][j-1] + sigma
    
    for i in range(1, s2+1): 
        for j in range(1, s1+1): 
            # only change here is the 0 option for the local alignment
            alignmentScores[i][j] = max(0,
                                        alignmentScores[i-1][j] + sigma,
                                        alignmentScores[i][j-1] + sigma, 
                                        alignmentScores[i-1][j-1] + PAM250[str1[j-1]][str2[i-1]])
      
    # backward output sequence here 
    # the idea here is to move backwards from alignmentScores[s2][s1] to 0.
    # if it moves up == deletion of s2 to s1, left == insertion of s2 to s1, diagonal is mismatches or matches doesn't matter
    finalScore = max(map(max, alignmentScores))
    maxPositions = list()
    sequenceScore = alignmentScores[s2][s1] 

    # finding the position of the max value - still trying to understand numpy here 
    for i in range(0, s2+1): 
        for j in range(0, s1+1): 
            if alignmentScores[i][j] == finalScore:
                maxPositions = [int(i),int(j)]
                
    # creating and parsing the conserved regions using the indices of the max position
    # then backtrack using them
    s2 = maxPositions[0]
    s1 = maxPositions[1]
    firstSequence = str1[:s1]
    secondSequence = str2[:s2]
    while sequenceScore != 0:
        # checking if there's a match so i can skip
        if ((sequenceScore) - PAM250[str1[s1-1]][str2[s2-1]] == alignmentScores[s2-1][s1-1]):
            s1-=1
            s2-=1
        else:
            # how do I tell the difference between which sigma it is? 
            if ((sequenceScore) - sigma == alignmentScores[s2-1][s1]):
                s2-=1                
                firstSequence = firstSequence[:s1] + '-' + firstSequence[s1:]

            elif ((sequenceScore) - sigma == alignmentScores[s2][s1-1]):
                s1 -= 1
                secondSequence = secondSequence[:s2] + '-' + secondSequence[s2:]

            else: 
                s1-=1
                s2-=1
        sequenceScore = alignmentScores[s2][s1]
    # this is to accurately cut off the beginning part of the two sequences
    firstSequence = firstSequence.replace(str1[:s1], "")
    secondSequence = secondSequence.replace(str2[:s2], "")

    # prepending or appending the -, last check 
    # this might be an issue so we'll see what happens here
    # firstSequence, secondSequence = applyIndel(firstSequence, secondSequence, len(str2) > len(str1))
    print(finalScore)
    print(firstSequence)
    print(secondSequence)
    printMatrix(str1, str2, alignmentScores)
    return finalScore, [firstSequence, secondSequence]

# this is a common dp problem actually
def editDistance(str1, str2):
    # base case if there is nothing to compare 
    if len(str1) == 0 or len(str2) == 0: 
        return 0
    s1 = len(str1)
    s2 = len(str2)
    
    alignmentScores = [[0 for j in range(s1+1)] for i in range(s2+1)]

    for i in range(1, s2+1):
        alignmentScores[i][0] = alignmentScores[i-1][0] + 1 

    for j in range(1, s1+1):
        alignmentScores[0][j] = alignmentScores[0][j-1] + 1
    
    for i in range(1, s2+1): 
        for j in range(1, s1+1): 

            if str2[i-1] == str1[j-1]:
                alignmentScores[i][j] = alignmentScores[i-1][j-1]
            else: 
                alignmentScores[i][j] = min(alignmentScores[i-1][j] + 1,
                                        alignmentScores[i][j-1] + 1, 
                                        alignmentScores[i-1][j-1] + 1)
    return alignmentScores[s2][s1]

# fitting alignment 
# basically global and local alignment won't work as it tries to align globally and locally
# local alignment will not fit the substring into a nice one because on indels
# when those indels could be key in producing a conserved region
# using the same idea as edit distance to produce the number of changes
# i think this uses global alignment to convert it and parse the region
def fittingAlignment(v, w):
    # base case if there is nothing to compare 
    if len(v) == 0 or len(w) == 0: 
        return 0
    s1 = len(v)
    s2 = len(w)
    
    alignmentScores = [[0 for j in range(s1+1)] for i in range(s2+1)]

    for i in range(1, s2+1): 
        for j in range(1, s1+1): 
            if w[i-1] != v[j-1]:
                alignmentScores[i][j] = max(alignmentScores[i-1][j] + -1,
                                        alignmentScores[i][j-1] + -1,
                                        alignmentScores[i-1][j-1] + -1)
            elif w[i-1] == v[j-1]:
                alignmentScores[i][j] = alignmentScores[i-1][j-1] + 1

    maxScore = 0
    # right now im assuming that s1 is greater in length than s2 
    # trying to find the max score in the last row
    for i in range(s1+1):
        if maxScore < alignmentScores[s2][i]:
            maxScore = alignmentScores[s2][i]
    maxPositions = list()
    # finding the position of the max value - still trying to understand numpy here 
    for i in range(0, s2+1): 
        for j in range(0, s1+1): 
            if alignmentScores[i][j] == maxScore:
                maxPositions = [int(i),int(j)]
    
    # don't know where to stop exactly with the beginning part
    s1 = maxPositions[1]
    s2 = maxPositions[0]
    v = v[:s1]
    w = w[:s2]
    sequenceScore = alignmentScores[s2][s1]

    # backtrack here
    while s1 != 0 and s2 != 0:
        if sequenceScore + 1 == alignmentScores[s2-1][s1]:
            s2-=1
            v = v[:s1] + '-' + v[s1:]
        elif sequenceScore + 1 == alignmentScores[s2][s1-1]:
            s1-=1
            w = w[:s2] + '-' + w[s2:]
        elif sequenceScore + 1 == alignmentScores[s2-1][s1-1]:
            s1 -=1 
            s2 -=1
        elif sequenceScore - 1 == alignmentScores[s2-1][s1-1]:
            s1-=1
            s2-=1
        sequenceScore = alignmentScores[s2][s1]
        
    # meaning there is something off and s1 is bigger than s2
    if len(v) != len(w):
        a = abs(len(v) - len(w))
        v = v[a:] 
        print(len(v), len(w), a)

    print(maxScore)
    print(v)
    print(w)


def overlapAlignment(v, w):
    # base case if there is nothing to compare 
    if len(v) == 0 or len(w) == 0: 
        return 0

    if len(v) < len(w):
        overlapAlignment(w,v)
        return
         

    s1 = len(v)
    s2 = len(w)
    
    alignmentScores = [[0 for j in range(s1+1)] for i in range(s2+1)]
    maxScore = -10000
    maxPositions = list()
    for i in range(1, s2+1): 
        for j in range(1, s1+1): 
            if w[i-1] != v[j-1]:
                alignmentScores[i][j] = max(alignmentScores[i-1][j] + -2,
                                        alignmentScores[i][j-1] + -2,
                                        alignmentScores[i-1][j-1] + -2)
            elif w[i-1] == v[j-1]:
                alignmentScores[i][j] = alignmentScores[i-1][j-1] + 1
    
    print(maxScore)
    maxScore = max(alignmentScores[-1])
    for i in range(0, s2):
        if maxScore < alignmentScores[i][-1]:
            maxScore = alignmentScores[i][-1]

    for i in range(0, s2):
        for j in range(0, s1):
            maxPositions = [i, j]

    # don't know where to stop exactly with the beginning part
    s1 = maxPositions[1]
    s2 = maxPositions[0]
    v = v[:s1+1]
    w = w[:s2]
    sequenceScore = alignmentScores[s2][s1]

    # backtrack here
    while s1 != 0 and s2 != 0:
        if sequenceScore + 2 == alignmentScores[s2-1][s1]:
            s2-=1
            v = v[:s1] + '-' + v[s1:]
        elif sequenceScore + 2 == alignmentScores[s2][s1-1]:
            s1-=1
            w = w[:s2] + '-' + w[s2:]
        elif sequenceScore + 2 == alignmentScores[s2-1][s1-1]:
            s1 -=1 
            s2 -=1
        elif sequenceScore - 1 == alignmentScores[s2-1][s1-1]:
            s1-=1
            s2-=1
        sequenceScore = alignmentScores[s2][s1]
        
    # meaning there is something off and s1 is bigger than s2
    if len(v) != len(w):
        a = abs(len(v) - len(w))
        v = v[a:] 
        print(len(v), len(w), a)

    print(maxScore, maxPositions)
    print(v)
    print(w)
    print("\n")
