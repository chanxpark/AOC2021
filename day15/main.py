class Cavern(): 
    def __init__(self, map): 
        self.map = map
        self.marked = [(0,0)]
        self.risk = 0 

    def printMap(self):
        for r in range(len(self.map)): 
            for c in range(len(self.map[0])): 
                if (r,c) in self.marked: 
                    print(f'\033[95m' + str(self.map[r][c]) + '\033[0m', end="")
                else: 
                    print(self.map[r][c], end="")
            print()
    
    def addMark(self, mark): 
        self.marked.append(mark)

    def findExit(self): 
        end = (len(map)-1, len(map[0])-1) 
        curr = (0, 0)
        while True: 
            # coordinates for left bottom
            DR = [1, 0]
            DC = [0, 1]
            min = 9999 
            next = None
            for k in range(len(DR)): 
                RR = curr[0] + DR[k]
                CC = curr[1] + DC[k]
                if map[RR][CC] <= min: 
                    min = map[RR][CC]
                    next = (RR, CC)
            curr = next
            self.addMark(curr)
            self.printMap()

if __name__ == "__main__": 
    f = "test.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n")]

    map = []

    for line in lines: 
        map.append([ int(n) for n in list(line) ])

    C = Cavern(map)
    C.findExit()