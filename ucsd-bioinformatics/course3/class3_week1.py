
""" 
    This is a library-like program that holds all of the functions for week 1 of class 3 
    source: bioinformatics course from ucsd on coursera
    this is the third part of part 1 - Genomics Sequenecing

"""

# this is a dp program on coin changing
def dpchange(money, listOfCoins):
    minNumCoins = dict() 
    minNumCoins[0] = 0
    for m in range(1, money + 1): 
        minNumCoins[m] = 100000
        for j in listOfCoins: 
            if m >= j: 
                if minNumCoins[m - j] + 1 < minNumCoins[m]: 
                    minNumCoins[m] = minNumCoins[m - j] + 1 
    return minNumCoins

# 1.6 problems and examples 
# this program is a modification of the longest sequence path
# it's kind of weirdly set up with stepik tho so oh well
### this does not handle diagonal crosses
# with the example from stepik, the answer is 34
# sequence is 0 1 4 10 17 22 30 32 34 
def manhattanTourist(n, m, down, right): 
    s = [[0 for j in range(m+1)] for i in range(n+1)]
    
    for i in range(1, n+1): 
        s[i][0] = s[i-1][0] + down[i-1][0]
        
    for j in range(1, m+1): 
        s[0][j] = s[0][j-1] + right[0][j-1] 
    
    for i in range(1, n+1): 
        for j in range(1, m+1):
            print(i,j)
            s[i][j] = max(s[i -1][j] + down[i-1][j], s[i][j-1] + right[i][j-1]) 

    return s[n][m] 

