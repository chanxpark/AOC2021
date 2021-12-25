from collections import defaultdict, Counter

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        L = [ n for n in input.read().strip().split("\n\n")]

    R = defaultdict(list) # rules
    RR = defaultdict(list) # new rules

    lines = L[1].strip().split("\n")
    for l in lines: 
        tmp = l.strip().split(" -> ")
        R[tmp[0]] = tmp[1]

    T = list(L[0]) # template

    """ # PART ONE
    steps = 10 
    i = 0 
    while i < 10: 
        print(f"steps: {i+1}")

        tmp = []
        for n in range(0, len(T)-1): 
            tmp.append(T[n])
            pair = T[n]+T[n+1]
            if pair in R.keys(): 
                tmp.append(R[pair])
        
        tmp.append(T[-1])
        T = tmp
        i += 1 
        # print(f"After step {i+1}: {T}")
    """

    C1 = defaultdict(int)

    # count all pairs
    for n in range(len(T)-1): 
        pair = T[n]+T[n+1]
        C1[pair] += 1

    # insert on all pairs for each step 
    for step in range(40): 
        print(f"step {step+1}")
        C2 = defaultdict(int)
        for n in C1: 
            C2[n[0]+R[n]] += C1[n]
            C2[R[n]+n[1]] += C1[n]

        C1 = C2 
    
    # count letters 
    C = Counter() 
    for c in C1: 
        C[c[0]] += C1[c]
    C[c[1]] += 1
    print(max(C.values()) - min(C.values()))
