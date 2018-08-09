
def chrToCycleNodes(nodes):
    chromosomes = [0] * int(len(nodes) / 2)
    for j in range( int(len(nodes) / 2)):
        if nodes[2 * j] < nodes[2 * j + 1]:
            chromosomes[j] = int(nodes[2 * j] / 2) + 1
        else:
            chromosomes[j] = int(-(nodes[2 * j + 1] / 2)) - 1 
    return chromosomes

def main():
    with open("input.txt", "r") as f:
        content = ((f.readline().strip("\n")).strip("(").strip(")")).split()
        content = list(map(int, content))
        content = chrToCycleNodes(content)
        a = "("
        for i in content: 
            if i >= 0:
                a += "+{} ".format(i)
            else:
                a += "{} ".format(i)
        a += ")"
        print(a) 

if __name__ == "__main__":
    main()