import fileinput
from typing import List

def createArray(file: str) -> List[int]: 
    result: List[int] = []
    for f in fileinput.input(file):
        result.append(int(f))

    return result

def partOne(arr: List[int]) -> int: 
    result: int = 0 
    prev: int = arr[0]
    for n in range(1, len(arr)): 
        if arr[n] > prev: 
            result += 1 
        prev = arr[n]

    return result

def partTwo(arr: List[int]) -> int: 
    result: int = 0 
    prev = sum(arr[0:3])
    for n in range(1, len(arr) - 2): 
        curr = sum(arr[n:n+3])
        if curr > prev: 
            result += 1
        prev = curr
    return result

if __name__ == "__main__": 
    f = "./input.txt"
    arr = createArray(f)
    print(partOne(arr))
    print(partTwo(arr))