def printMap(map): 
    for r in map: 
        for c in r: 
            print(c, end="")
        print()
    print()

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = input.read().strip().split("\n")
    
    map = []
    for line in lines: 
        map.append(list(line))

    # once left, once down 
    rows = len(map)
    cols = len(map[0])
    steps = 0
    moved = True
    while moved: 
        print(steps)
        moved = False
        for i in range(2):
            new_map = [ ["."] * cols for _ in range(rows) ] 
            for r in range(rows): 
                for c in range(cols): 
                    # get next value 
                    if i == 0: 
                        if map[r][c] == "v": 
                            new_map[r][c] = "v"
                        if map[r][c] == ">": 
                            cc = c + 1 if c != cols-1 else 0 
                            if map[r][cc] == ".": 
                                new_map[r][cc] = ">"
                                moved = True
                            else: 
                                new_map[r][c] = ">"
                    if i == 1: 
                        if map[r][c] == ">": 
                            new_map[r][c] = ">"
                        if map[r][c] == "v": 
                            rr = r + 1 if r != rows-1 else 0 
                            if map[rr][c] == ".": 
                                new_map[rr][c] = "v"
                                moved = True
                            else: 
                                new_map[r][c] = "v"
            map = new_map

        steps += 1 
    print(f"after {steps} steps")
    printMap(map)