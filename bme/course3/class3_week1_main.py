""" 
    This is for the testing of class 3 programs 
    Input: None 
    Output: Depends on which section is uncommented or not 


    Will try and implement a testing unit for this class instead to make it easier to work with 
    and that I could learn how to unit test in python 

    Many of these programs/functions will be implemented without the use of libraries to 
    get myself thinking about it thus reinventing the wheel 
        1. will decide to put up a library alternative in case for other analysis
"""

from class3_week1 import *
import sys, os

def main(): 
    # 1.5 section - intro to dp, coin change problem 
    # minCoins = dpchange(40, [50, 25, 20, 10, 5, 1]) 
    # print(minCoins)

    # for testing time set 1.5
    # with open(sys.argv[1], 'r') as f: 
    #     money = int(f.readline()) # reading in money 
    #     content = f.readline() # reading in listofCoins 
    #     coins = list(map(int, content.split(',')))
    #     minCoins = dpchange(money, coins)
    #     print(minCoins[money])

    # 1.6 section - manhattan tourist time 
    with open(sys.argv[1], 'r') as f: 
        content = f.readline() 
        content = (content.strip('\n')).split() 
        down = list() 
        right = list() 
        for i in f: 
            if '-' in i:
                break
            entry = list(map(int, (i.strip('\n')).split()))
            down.append(entry) 
        for i in f: 
            entry = list(map(int, (i.strip('\n')).split()))
            right.append(entry)
        a = manhattanTourist(int(content[0]), int(content[1]), down, right)
        print(a)


if __name__ == "__main__": 
    main()