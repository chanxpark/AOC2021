import fileinput

def main(file) -> int: 
    first: bool = True
    result: int = 0 
    prev: int = 0
    for f in fileinput.input(file):
        val = int(f)
        if val > prev and not first: 
            result += 1
        
        prev = val
        first = False

    return result

if __name__ == "__main__": 
    f = "./input.txt"
    print(main(f))