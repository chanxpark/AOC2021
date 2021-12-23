from typing import List

def partOne(X): 
    X.sort()

    ans = 0 
    med = X[len(X)//2]
    for x in X: 
        ans += abs(x - med)

    return ans

def calcFeul(X, avg): 
    ans = 0 
    for x in X: 
        feul = 0 
        for i in range(abs(x-avg)+1): 
            feul += i
        ans += feul
    
    return ans

def partTwo(X): 
    
    floor_avg = sum(X)//len(X)
    ceil_avg = round(sum(X)/len(X))
    floor_ans = calcFeul(X, floor_avg)
    ceil_ans = calcFeul(X, ceil_avg)

    return min(floor_ans, ceil_ans)
    

if __name__ == "__main__": 
    f = "input.txt"
    with open(f, "r") as input: 
        lines: List[int] = [ int(n) for n in input.read().strip().split(",")]

    # print(partOne(lines))
    print(partTwo(lines))