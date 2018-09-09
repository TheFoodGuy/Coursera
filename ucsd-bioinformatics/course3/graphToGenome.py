"""
GraphToGenome(GenomeGraph)
    P ← an empty set of chromosomes
    for each cycle Nodes in GenomeGraph
        Nodes﻿ ← sequence of nodes in this cycle (starting from node 1)
        Chromosome ← CycleToChromosome(Nodes)
        add Chromosome to P
    return P

    Input: (2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)
    Output: (+1 -2 -3)(-4 +5 -6)


"""

from chrToCycle import chrToCycle 
from chrToCycleNodes import chrToCycleNodes
def graphToGenome(genomeGraph):
    # base case assumming only at most themselves or 1 other works 
    p = []
    for i in range(len(genomeGraph)-1):
        for j in range(i, len(genomeGraph)):
            if abs(genomeGraph[i][1] - genomeGraph[j][0]) == 1:
                p.append([genomeGraph[i], genomeGraph[j]])
                break

    # print(p)      
    
    # fixing the overlapping issues here
    while(True):
        indicesToDel = list()
        statusP = p
        for i in range(len(p)-1):
            for j in range(i+1, len(p)): 
                # print(p[i], p[j])
                if (abs(p[i][len(p[i]) - 1][1] - p[j][len(p[j]) - 1][0]) == 1):
                    tmpP = p[i] + [[p[j][len(p[j]) - 1][0], p[j][len(p[j]) - 1][1]]]
                    p[i] = tmpP
                    indicesToDel.append(j)

        if statusP == p:
            break
    # checking the last item to be sure

    newP = list()
    # print("new at the moment ->", p)
    # print("checking ->", indicesToDel)
    for i in range(len(p)):
        if i not in indicesToDel:
            newP.append(p[i])

    p = [] 
    for cycle in newP:
        currentCycle = list()
        for orderedPair in cycle:
            currentCycle.append(orderedPair[0])
            currentCycle.append(orderedPair[1])
        p.append(currentCycle)
    # now im converting this back to their genome form corresponding to the graph 
    # doing some clean up and moving all last element to the front and deleting it from the back
    for index in range(len(p)):
        p[index] = [p[index][-1]] + p[index][ : len(p[index]) - 1]
    
    print(p)
    # now doing some maths here for the final conversions
    genomes = list()
    for cycle in p:
        cycleOutput = chrToCycleNodes(cycle)
        genomes.append(cycleOutput)
    return(genomes)

def main(): 
    with open("input.txt", "r") as f:
        content = (f.readline()).split(",")
        newContent = list()
        for i in content:
            if i.strip() != "":
                i = i.strip().strip("(").strip(")")
                newContent.append(i)
        newContent = list(map(int, newContent))
        content = [[newContent[i],newContent[i+1]] for i in range(0,len(newContent),2)]
        # print(content)
        genomes = graphToGenome(content)
        # trying to print now 
        currentGenome = ""
        for genome in genomes:
            currentGenome += "("
            for i in genome:
                if i >= 0:
                    currentGenome += "+{} ".format(i)
                else:
                    currentGenome += "{} ".format(i)
            currentGenome = currentGenome.rstrip()
            currentGenome += ")"
        # print(currentGenome)
        

                

if __name__ == "__main__":
    main()