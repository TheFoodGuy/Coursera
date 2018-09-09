from chrToCycle import chrToCycle 

def coloredEdges(P):
    edges = []
    for chr in P:
        nodes = chrToCycle(chr)
        nodes.append(nodes[0])
        for j in range(0, len(chr)):
            coordNodeX = nodes[2 * j+1] 
            coordNodeY = nodes[2 * j+2]
            
            edges.append([coordNodeX, coordNodeY])
    # print (', '.join(str(x) for x in edges))
    return edges

def main():
    with open("input.txt", "r") as f:
        content = f.readline().strip("\n")
        content = (content.split("("))
        content = [x.replace(")", "") for x in content if x and ")" in x]
        newContent = list() 

        for cont in content:
            newCont = cont.split()
            newCont = list(map(int, newCont))
            newContent.append(newCont) 
        content = coloredEdges(newContent)
        a = ""
        for i in content:
            a += "({}, {}), ".format(i[0], i[1])
        print(a)

if __name__ == "__main__":
    main()