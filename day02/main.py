import fileinput
from typing import List

def partOne(file) -> int: 
    h: int = 0 # horizontal
    d: int = 0 # depth
    for f in fileinput.input(file): 
        val: List[str] = f.split()
        if val[0] == "forward": 
            h += int(val[1])
        elif val[0] == "down":
            d += int(val[1])
        else: 
            d -= int(val[1])
        
    return d * h

def partTwo(file) -> int: 
    h: int = 0 # horizontal
    d: int = 0 # depth
    a: int = 0 # aim 
    for f in fileinput.input(file): 
        val: List[str] = f.split()
        if val[0] == "forward": 
            h += int(val[1])
            d += int(val[1]) * a
        elif val[0] == "down":
            a += int(val[1])
        else: 
            a -= int(val[1])
        
    print(d, h)
    return d * h

if __name__ == "__main__": 
    f = "./input.txt"
    print(partOne(f))
    print(partTwo(f))