from typing import TYPE_CHECKING


if __name__ == "__main__": 
    f = "test.txt"

    with open(f, "r") as input: 
        lines = input.read().strip().split("\n")

    # [on/off, (x, x), (y, y), (z, z)]

    commands = []
    
    for line in lines: 
        L = line.strip().split(" ")
        command = [L[0]]
        for l in L[1].strip().split(","): 
            ll = l.strip().split("=")
            lll = ll[1].strip().split("..") 
            command += [ (int(lll[0]), int(lll[1])) ] 
        commands.append(command)
    
    # arr = [-50, 50]
    # len(arr)/2 + pos = the position of the value

    n = 50 * 2 + 1
    m = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    POS = n // 2
    for c in commands: 
        if c[1][0] < -50 or c[2][0] < -50 or c[3][0] < -50:
            continue 
        if c[1][1] > 50 or c[2][1] > 50 or c[3][1] > 50:
            continue

        for x in range(c[1][0], c[1][1]+1): 
            for y in range(c[2][0], c[2][1]+1): 
                for z in range(c[3][0], c[3][1]+1): 
                    m[POS+x][POS+y][POS+z] = 1 if c[0] == "on" else 0
    
    # get # of cubes
    s = 0 
    for i in m: 
        for j in i: 
            s += sum(j)

    print(s)
        