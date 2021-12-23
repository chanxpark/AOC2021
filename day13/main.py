def printMap(map): 
    for row in range(len(map)): 
        for col in range(len(map[0])): 
            print(map[row][col], end="")
        print()

def drawMap(dots, col_size, row_size):
    count = 0  
    map = [ ["."] * (col_size) for _ in range(row_size) ]
    
    for d in dots:
        if map[d[1]][d[0]] != "#": 
            map[d[1]][d[0]] = "#"
            count += 1

    return (count, map)

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n\n")]

    # dots 
    D = [ n for n in lines[0].strip().split("\n") ]
    dots = [] # (col, row)
    for d in D: 
        t = d.strip().split(",")
        c = int(t[0])
        r = int(t[1])
        dots.append((c, r))
   
    # folds
    F = [ n for n in lines[1].strip().split("\n") ]
    folds = [] # (axis, num)
    for f in F: 
        t = f.strip().split(" ")
        tt = t[2].strip().split("=")
        folds.append((tt[0], int(tt[1])))
    
    # do folds 
    # get size of map 
    col_size = 0 
    row_size = 0
    for d in dots:     
        if d[0] > col_size: 
            col_size = d[0]
        if d[1] > row_size: 
            row_size = d[1]
    col_size += 1
    row_size += 1

    c = 0 
    for f in folds: 
        if f[0] == "y": 
            row_size = f[1]
            for i, d in enumerate(dots): 
                if d[1] > f[1]: 
                    dots[i] = (d[0], f[1] - (d[1] - f[1]))

        elif f[0] == "x": 
            col_size = f[1]
            for i, d in enumerate(dots): 
                if d[0] > f[1]:
                    dots[i] = (f[1] - (d[0] - f[1]), d[1])
        
        c += 1 
        print(f"folds: {c}")
        ans = drawMap(dots, col_size, row_size)
        printMap(ans[1])
        print(f"ans: {ans[0]}\n")    