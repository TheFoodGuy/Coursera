"""
    week 3 is basically a much more emphasized idea of dp from week2 but more towards 
    pairwise and multisequence alignment algorithms and how to be much more efficient
"""
import sys, os
from class3_week3 import *
rfile = ''
if len(sys.argv) == 1:
    rfile = 'input.txt'
else: 
    rfile = sys.argv[1]

with open(rfile, 'r') as f:
    entry1 = (f.readline()).strip('\n')
    entry2 = (f.readline()).strip('\n')
    # affineGapAlignment()
    affineGapAlignment(entry1, entry2)
