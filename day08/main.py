from typing import List

def partOne(codes): 
    key = [2,3,4,7]
    ans = 0 
    for code in codes: 
        for c in code.strip().split(" "): 
            if len(c) in key: 
                ans += 1 

    return ans 

if __name__ == "__main__": 
    f = "test.txt"
    with open(f, "r") as input: 
        lines: List[int] = [ n for n in input.read().strip().split("\n")]
    codes = []
    for line in lines: 
        t = line.strip().split("|")
        codes.append(t[1])
    print(partOne(codes))