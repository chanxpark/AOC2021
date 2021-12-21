from typing import List

def printMap(map): 
    for row in map: 
        for n in row: 
            print(n,end='')
        print("")

def findLows(map): 
    low = []

    for i in range(len(map)): 
        for j in range(len(map[i])):
            p = [] # points
            col_start = 0
            col_end = 0 
            if j == 0: 
                col_start = j
                col_end = j+2 
                p += map[i][col_start:col_end]
            else: 
                col_start = j-1
                col_end = j+2 
                p += map[i][col_start:col_end]
            
            if map[i][j] == min(p): 
                if i != 0: 
                    p += map[i-1][col_start:col_end]
                if i != len(map)-1: 
                    p += map[i+1][col_start:col_end]
                if map[i][j] == min(p): 
                    low.append((i,j))

    return low 

if __name__ == "__main__": 
    f = "test.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n")]

    map = []
    for line in lines: 
        map.append([ int(n) for n in list(line) ])

    print(findLows(map))