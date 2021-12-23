from typing import List

counter = 0

def printMap(map): 
    for r in map: 
        for c in r: 
            print(c, end="")
        print()

def adj(r, c, map) -> List[int]: 
    # top left clock wise
    DR = [-1, -1, -1, 0, 1, 1,  1,  0]
    DC = [-1,  0,  1, 1, 1, 0, -1, -1]
    
    neighbors = []
    for d in range(len(DR)):
        RR = r + DR[d]
        CC = c + DC[d]
        if 0 <= RR and 0 <= CC and RR <= len(map)-1 and CC <= len(map[0])-1: 
            neighbors.append((RR, CC)) 
    
    return neighbors

def flash(r,c, map): 
    global counter
    counter += 1
    map[r][c] = -1

    neighbors = adj(r,c,map)

    for n in neighbors: 
        RR = n[0]
        CC = n[1]
        if map[RR][CC] != -1: 
            map[RR][CC] += 1
            if map[RR][CC] >= 10: 
                flash(RR, CC, map)

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n")]

    map = []
    for line in lines: 
        map.append([ int(n) for n in line ])
    
    counter = 0 

    steps = 100
    printMap(map)

    R = len(map)
    C = len(map[0])

    # for step in range(steps):
    step = 0
    while True:
        step += 1 
        synced = True
        print(f"{step}")
        for r in range(R): 
            for c in range(C): 
                map[r][c] += 1
        for r in range(R): 
            for c in range(C): 
                if map[r][c] >= 10: 
                    flash(r, c, map)
        for r in range(R): 
            for c in range(C): 
                if map[r][c] == -1: 
                    map[r][c] = 0
                else: 
                    synced = False

        printMap(map)

        if synced: 
            print(step)
            break

    print(f"ans: {counter}")
    

    
