from typing import List
from collections import Counter

if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = [ n for n in input.read().strip().split("\n")]

    i = {
        ")": "(", 
        "]": "[",
        "}": "{",
        ">": "<"
    }

    I = {
        "(": ")", 
        "[": "]",
        "{": "}",
        "<": ">"
    }

    CS = {
        ")": 3, 
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    IS = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    tmp = 0 

    corrupted_ans = 0
    incomplete_ans = []
    for line in lines: 
    # line = "<{([([[(<>()){}]>(<<{{"
        corrupted = False 
        T = []
        for c in line: 
            if c in "([{<": 
                T.append(c)
            if c in ")]}>": 
                if i[c] in T[-1]: 
                    T.pop()
                else: 
                    corrupted_ans += CS[c]
                    corrupted = True
                    break

        if not corrupted: 
            tmp = 0 
            # print("".join(T))
            for t in range(len(T)):
                # print(I[T[-1]], end="")
                tmp = (tmp * 5) + IS[I[T[-1]]]
                T.pop()
            incomplete_ans.append(tmp)

    print(f"corrupted: {corrupted_ans}")
    incomplete_ans.sort()
    ans = incomplete_ans[len(incomplete_ans)//2]
    print(f"incomplete: {ans}")