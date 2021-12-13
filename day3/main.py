import fileinput
from typing import List

# creates an array of binary values based on stdin
def createArr(file: str) -> List[List[int]]: 
    result: List[List[int]] = []
    for f in fileinput.input(file): 
        result.append([int(ch) for ch in f.strip()])
    
    return result

# finds the most common bit in X position
def findMCB(arr: List[List[int]], pos: int) -> int: 
    # sum of bits in X position
    result = 0 
    for n in arr: 
        result += n[pos]
    
    return 1 if result/len(arr) >= .5 else 0

def partOne(file) -> int: 
    # find the sum of 
    count: int = 0 # counts the total length of input 
    first: bool = True # flag to know if its first loop or not
    for f in fileinput.input(file): 
        if first: 
            sums: List[int] = (len(f) - 1) * [0] # array to hold the sum of each bit
        for i, v in enumerate(f.strip()):
            sums[i] += int(v)

        first = False
        count += 1
    
    m: int = 0 # decimal value of most common bit
    l: int = 0 # decimal value of least common bit

    # determine the most and least common bit
    # convert to decimal
    for i, v in enumerate(sums): 
        b: int = round(v/count) # most common bit
        m += b * pow(2, len(sums)-1-i)
        # b^1 returns the complement of b or the least common bit
        l += (b^1) * pow(2, len(sums)-1-i)
    
    return l * m

def partTwo(file) -> int: 
    arr: List[List[int]] = createArr(file)

    # oxygen generator rating (most common bit)
    ogr: List[List[int]] = arr 
    i = 0
    while len(ogr) > 1: 
        mcb = findMCB(ogr, i)
        tmp: List[List[int]] = []
        ogr = [ tmp.append(n) for n in ogr if n[i] == mcb ]
        ogr = tmp
        i += 1  

    # CO2 scrubber rating (least common bit)
    csr: List[List[int]] = arr 
    i = 0
    while len(csr) > 1: 
        lcb = findMCB(csr, i)^1 # take complement of most common bit 
        tmp: List[List[int]] = []
        csr = [ tmp.append(n) for n in csr if n[i] == lcb ]
        csr = tmp
        i += 1  
    
    # convert values to decimal
    o: int = 0 # ogr decimal value
    c: int = 0 # ogr decimal value
    for i in range(len(ogr[0])): o += ogr[0][i] * pow(2, len(ogr[0])-1-i); c += csr[0][i] * pow(2, len(ogr[0])-1-i)

    return o * c

if __name__ == "__main__": 
    f = "./input.txt"
    print("Part 1:", partOne(f))
    print("Part 2:", partTwo(f))