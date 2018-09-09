# this is needed to import the matrices and I don't want to recopy it all the time - waste spaces 
from class3_week2 import *
import numpy as np
from copy import copy, deepcopy

""" I would say this is a modification of the global alignment to produce a better pairwise search 
    over the issue of having multiple same score solution to get a better biological sequence that makes sense 

    Input: 2 strings 
    Output: final Score of the two strings and the two strings after modificaitons
    EX. v and w are set to the default args
        8
        PRT---EINS
        PRTWPSEIN- 

    NOTE: Imma follow the way the reccurence relation is set up otherwise i would have 
    used one 2D matrix for this problem with a tuple as the key for dictionary
"""
def affineGapAlignment(v = 'PRTEINS', w='PRTWPSEIN'):
    lenV = len(v)+1
    lenW = len(w)+1
    
    sigma = -11 
    espilon = -1

    mScores = np.zeros(shape=(lenW, lenV),dtype='int')
    dScores = np.zeros(shape=(lenW, lenV),dtype='int')
    iScores = np.zeros(shape=(lenW, lenV),dtype='int')
    scoreMatrix = getVariable(BLOSUM62)

    # initializing the graphs here 
    iScores[0][0] = sigma 
    dScores[0][0] = sigma
    for i in range(1, lenW):
        dScores[i][0] = dScores[i-1][0] + espilon
        mScores[i][0] = mScores[i-1][0] + espilon
        iScores[i][0] = -100000

    for j in range(1, lenV):
        # # mScores[0][j] = mScores[0][j-1] + espilon
        iScores[0][j] = iScores[0][j-1] + espilon
        mScores[0][j] = mScores[0][j-1] + espilon
        dScores[0][j] = -100000 


    for i in range(1, lenW):
        for j in range(1, lenV):
        
            dScores[i][j] = max(dScores[i-1][j] + espilon,
                                mScores[i-1][j] + sigma)

            iScores[i][j] = max(iScores[i][j-1] + espilon,
                                mScores[i][j-1] + sigma)
                                
            mScores[i][j] =  max(mScores[i-1][j-1] + scoreMatrix[v[j-1]][w[i-1]],
                                iScores[i][j],
                                dScores[i][j])

    maxScore = mScores[lenW-1][lenV-1]
    sequenceScore = mScores[lenW-1][lenV-1]
    lenV1 = lenV-1 
    lenW1 = lenW-1
    status = [0, 1, 0]
    
    while lenV1 != 0 and lenW1 != 0:
        print(lenV1, sequenceScore)
        if status[1] == 1: 
            if sequenceScore+ scoreMatrix[v[lenV1-1]][w[lenW1-1]] == mScores[lenW1-1][lenV1-1]:
                lenV1-=1 
                lenW1-=1
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]

            # if it doesn't match or there's an indel somewhere
            elif sequenceScore+1 == dScores[lenW1-1][lenV1]:
                lenW1 -= 1
                v = v[:lenV1] + '-' + v[lenV1:]
                status = [1, 0, 0]
                sequenceScore = dScores[lenW1][lenV1]

            elif sequenceScore+1 == iScores[lenW1][lenV1-1]:
                lenV1 -= 1
                w = w[:lenW1] + '-' + w[lenW1:]
                status = [0, 0, 1]
                sequenceScore = iScores[lenW1][lenV1]

            elif sequenceScore+11 == mScores[lenW1-1][lenV1]:
                lenW1 -= 1
                v = v[:lenV1] + '-' + v[lenV1:]
                status = [0, 1, 0] #x
                sequenceScore = mScores[lenW1][lenV1]

            elif sequenceScore+11 == mScores[lenW1][lenV1-1]:
                lenV1 -= 1
                w = w[:lenW1] + '-' + w[lenW1:]
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]

            else:
                lenV1 -= 1 
                lenW1 -= 1
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]
        elif status[0] == 1:
            if sequenceScore+1 == dScores[lenW1-1][lenV1]:
                lenW1 -= 1 
                v = v[:lenV1] + '-' + v[lenV1:]
                status = [1, 0, 0]
                sequenceScore = dScores[lenW1][lenV1]

            elif sequenceScore + 11 == mScores[lenW1-1][lenV1]:
                lenW1 -= 1 
                v = v[:lenV1] + '-' + v[lenV1:]
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]

            else: 
                lenW1 -= 1 
                lenV1 -= 1 
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]

        elif status[2] == 1: 
            if sequenceScore+1 == iScores[lenW1][lenV1-1]:
                lenV1 -= 1 
                w = w[:lenW1] + '-' + w[lenW1:]
                status = [0, 0, 1]
                sequenceScore = iScores[lenW1][lenV1]

            elif sequenceScore+11 == mScores[lenW1][lenV1-1]:
                lenV1 -= 1 
                w = w[:lenW1] + '-' + w[lenW1:]
                status = [0, 1, 0 ]
                sequenceScore = mScores[lenW1][lenV1]

            else: 
                lenV1 -= 1 
                lenW1 -= 1 
                status = [0, 1, 0]
                sequenceScore = mScores[lenW1][lenV1]


    print(dScores)
    print(mScores)
    print(iScores)


    print(maxScore)    
    print(v)
    print(w)

