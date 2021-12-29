from typing import List

def printMap(map): 
    for row in map: 
        for n in row: 
            print(n,end='')
        print("")

def findLows(map): 
    low = []
    ans = 0 

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
                    ans += map[i][j] + 1 

    return (low, ans)

def findBasins(point, map, basin): 
    DR = [1, 0, -1, 0]
    DC = [0, 1, 0, -1]
    r = point[0]
    c = point[1]
    for k in range(4): 
        rr = r + DR[k]
        cc = c + DC[k]
        if rr >= 0 and cc >= 0 and rr < len(map) and cc < len(map[0]): 
            if map[rr][cc] < 9: 
                if (rr, cc) not in basin: 
                    basin.append((rr, cc))
                    findBasins((rr, cc), map, basin)
    
    return basin

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n")]

    map = []
    for line in lines: 
        map.append([ int(n) for n in list(line) ])

    L = findLows(map)
    # print(f"part one ans: {L[1]}")
    lows = L[0]

    max_basins = []
    for low in lows: 
        b = findBasins(low, map, [low])
        max_basins.append(len(b))
        max_basins.sort(reverse=True)
        max_basins = max_basins[:3]
    
    ans2 = 1
    for n in max_basins: 
        ans2 *= n
    
    print(f"part two ans: {ans2}")
