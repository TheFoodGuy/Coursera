"""
    Week 3 Course 3 - 1_Implement GreedySorting
    Input: A permutation P 
    Output: The sequence of permutations corresponding to applying GreedySorting to P,
            ending with the identity permutation 

    Ex. Input:  (-3 +4 +1 +5 -2)

        Ouput:  (-1 -4 +3 +5 -2) 
                (+1 -4 +3 +5 -2)
                (+1 +2 -5 -3 +4)
                (+1 +2 +3 +5 +4)
                (+1 +2 +3 -4 -5)
                (+1 +2 +3 +4 -5)
                (+1 +2 +3 +4 +5)

    # assumptions, by greedysorting, we would sort by the least value
    # so 1 goes first 2 goes first etc... to N
"""
import sys
def greedySorting(permutation):
    # importing permutation as a list
    content = (permutation.strip("(")).strip(")")
    content = [int(x) for x in content.split()]
    changes = list()
    
    approxreversalDistance = 0 
    k = 0
    for k in range(len(content)):
        # if their corresponding position isn't the same value then we need to sort
        if abs(content[k]) != (k+1):
            # swap the values
            tempList = list()
            tempList.append(-content[k])
            for i in range(k+1, len(content)):
                if abs(content[i]) != (k+1):
                    tempList.append(-content[i]) 
                else: 
                    tempList.append(-content[i]) 
                    tempList.reverse()
                    content[k:i+1] = tempList
                    changes.append(content[:])
            approxreversalDistance = approxreversalDistance + 1

        if content[k] < 0:
            content[k] = -content[k]
            changes.append(content[:])
            approxreversalDistance = approxreversalDistance + 1
                
    return approxreversalDistance, changes
    

# borrowed because of the issue people have been facing to print out 
# their outputs
def write_step(step, file_handle):
    file_handle.write('(')
    for i, elem in enumerate(step):
        elem_str = str(elem)
        if elem > 0:
            elem_str = '+' + elem_str
        if i != len(step)-1:
            elem_str += ' '
        file_handle.write(elem_str)
    file_handle.write(')\n')


def main():
    with open("input.txt", "r") as f:
        inputLine = (f.readline()).strip("\n")
        # greedySorting(inputLine)
        value, change = greedySorting(inputLine)
        [write_step(i, sys.stdout) for i in change]
if __name__ == "__main__":
    main()  