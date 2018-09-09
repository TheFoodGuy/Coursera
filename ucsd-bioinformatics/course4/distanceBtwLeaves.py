"""
    This is the first assignment for course 4 of week 1 for Molecular Evolution

    Input: A weighted tree with n leaves
    Output: An n x n matrix (dij) where dij is the length of the path
            between leaves i and j

    Comment: This problem is using DFS or BFS but it's a modified version of it 
    for implementation which is throwing me off all the suddne to be frank.
"""
import numpy as np
def distanceBtwLeaves(n, adj):
    # setting up the base case and the matrix
    adjList = np.array(adj)
    matrix = np.zeros(shape = (n,n))

    # each leaf is a starting point
    # endLeaf == destination 
    for leaf in range(n):
        for endLeaf in range(n):
            if leaf == endLeaf: 
                matrix[leaf][endLeaf] = 0
            else:
                 

def printMatrix(matrix):
    pass

# as usual, just parsing the data to go into distanceBtwLeaves. 
def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        adjList = []

        for line in f:
            content = line.split("->")
            content1 = content[1].split(":")
            adjList.append(list(map(int, [content[0], content1[0], content1[1]])))

        print("{}\n{}".format(n, adjList))
        distanceBtwLeaves(n, adjList) 

if __name__ == "__main__":
    main()

