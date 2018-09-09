
def chrToCycle(Chr):
    nodes = [0] * 2 * len(Chr)
    for j in range(len(Chr)):
        i = Chr[j]
        if i > 0:
            nodes[(2*j)] = 2 * i - 1 
            nodes[2*j+1] = 2 * i 
        else: 
            nodes[(2*j)] = -1 * 2 * i 
            nodes[(2*j) + 1] = -1 * 2 * i - 1
    return (nodes)

def main():
    with open("input.txt", "r") as f:
        content = ((f.readline().strip("\n")).strip("(").strip(")")).split()
        content = list(map(int, content))
        content = chrToCycle(content)
        a = "("
        for i in content: 
            a += "{} ".format(i)
        a += ")"
        print(a) 


if __name__ == "__main__":
    main()
