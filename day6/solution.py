# not my solution 
# from https://www.youtube.com/watch?v=fHlWM8CIrlI&ab_channel=CodingTech

from collections import Counter, defaultdict

def solve(fishes, days): 
    current = fishes
    for _ in range(days): 
        new = defaultdict(int)
        for fish, count in current.items(): 
            if fish == 0: 
                new[6] += count
                new[8] += count
            else: 
                new[fish-1] += count 
        
        current = new 
    
    return sum(current.values())

if __name__ == "__main__": 
    f = "input.txt"
    with open(f, "r") as input: 
        x = Counter([ int(n) for n in input.read().strip().split(",")])   

    print(solve(x, 80))
    print(solve(x, 256))