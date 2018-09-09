"""
    Course 3 Week 4 - 2_Find the number of breakpoints in a permutations
    Input: A permutation (signed)
    Output: The number of breakpoints in this permutation

    Ex. Input : (+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)
        Output : 8
"""
def findNumBreaks(permutation):
    breakNums = 0 
    for i in range(1, len(permutation)):
        if abs(permutation[i-1] - permutation[i]) != 1:
            breakNums += 1
    return breakNums 
def main():
    with open("input.txt" ,"r") as f: 
        p = f.readline()
        p = ((p.strip(")").strip("("))).strip("\n")
        p = [int(x) for x in p.split()]
        print(findNumBreaks(p))

if __name__ == "__main__":
    main()
 
