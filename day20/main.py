def printImage(image): 
    for r in image: 
        for c in r: 
            print(c, end="")
        print()
    print()

def binToDec(bin): 
    r = 0 
    bin.reverse()
    for i, n in enumerate(bin): 
        r += n * pow(2, i)
    return r 

def enhance(r, c, image): 
    # left to right, row by row 
    DR = [-1, -1, -1,  0, 0, 0,  1, 1, 1]
    DC = [-1,  0,  1, -1, 0, 1, -1, 0, 1]

    E = []
    val = 1 if image[0][0] == "#" else 0 
    for d in range(len(DR)):
        RR = r + DR[d]
        CC = c + DC[d]
        if 0 <= RR and 0 <= CC and RR < len(image) and CC < len(image[0]):
            E += [0] if image[RR][CC] == "." else [1]
        else: 
            E += [val]
    
    return binToDec(E)

def expand(image):
    for r in range(len(image)): 
        image[r] = ["."] + image[r] + ["."]

    new_row = [ ["."] * len(image[0]) ]

    return new_row + image + new_row


if __name__ == "__main__": 
    f = "input.txt"

    with open(f, "r") as input: 
        lines = input.read().strip().split("\n\n")

    enhancement = lines[0]

    image = []
    L = lines[1].strip().split("\n")
    for l in L: 
        image.append(list(l))

    for _ in range(50): 
        image = expand(image)

    for step in range(50): 
        new_image = [ [0] * len(image[0]) for _ in range(len(image)) ]
        pixels = 0 
        for r in range(len(image)): 
            for c in range(len(image[0])): 
                p = enhancement[enhance(r, c, image)]
                pixels += 1 if p == "#" else 0 
                new_image[r][c] = p 
        
        image = new_image
        print(f"after step: {step+1}")
        # printImage(image)
        print(f"count: {pixels}")

    # printImage(image)

    
    

    
