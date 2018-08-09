"""
    Compute the distances between leaves in a weighted tree 
    Input: An integer n (numLeaves) followed by the adjacency list of a weighted tree with n leaves 
    Output: An n x n matrix where dij is the length of the path between leaves i and j
"""
# Not too sure if n is always even to be honest, but let's assume that 
def distanceBetweenLeaves(n, adjacencyList):
    # matrix contains the output values 
    # fixedAdjacencyList contains the list but for usage 
    fixedAdjacencyList = list()
    matrix = list()
    for i in adjacencyList:
        tempDict = {} 
        tempDict[i[0]] = [i[1][0], i[1][1]]
        fixedAdjacencyList.append(tempDict)
    print(fixedAdjacencyList) 
    
    # time to make the tree here 
    # make sure to check if the tree is the same or not 
    # and if the tree hits log(n) 
    # make sure to check out dfs here tomorrow

def printMatrix(adjacencyList):
    matrix = ""
    for i in adjacencyList:
        for j in i:
            matrix = matrix + "{}\t".format(j)
        matrix = matrix + "\n"
    return matrix

def main():
    with open("input.txt", "r") as f:
        numLeaves = int(f.readline())
        adjacencyBranches = list()
        for line in f:
            content = (line.strip("\n")).split("->")
            toAndEdge = content[1].split(":")
            adjacencyBranches.append([content[0], toAndEdge])
    print(distanceBetweenLeaves(numLeaves, adjacencyBranches))


if __name__ == "__main__":
    main()
