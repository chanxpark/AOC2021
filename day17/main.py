def simulate (vx, vy): # returns (Y_MAX,(VX, VY))
    # targets 
    # test: target area: x=20..30, y=-10..-5
    # TARGET_X = [20, 30]
    # TARGET_Y = [-10, -5]
    # input: target area: x=138..184, y=-125..-71
    TARGET_X = [138, 184]
    TARGET_Y = [-125, -71]
    MAX_Y = 0 
    # initial values 
    i_vx = vx 
    i_vy = vy
    x = 0 
    y = 0 
    while x <= TARGET_X[1] and y >= TARGET_Y[0]: 
        # print(x,y)
        # calculate new x and y  
        x += vx
        y += vy 
        MAX_Y = max(MAX_Y, y)

        if TARGET_X[0] <= x <= TARGET_X[1] and TARGET_Y[0] <= y <= TARGET_Y[1]: 
            return (MAX_Y, (i_vx, i_vy))

        # calculate new vx and vy 
        if vx != 0: 
            x_increment = 1 if x >= 0 else -1
            vx -= x_increment
        vy -= 1 

    return (-1, (-1, -1)) 

if __name__ == "__main__": 
    S = 200
    MAX_Y = 0 
    valid = []
    for vx in range(S): 
        for vy in range(-S, S): 
            r = simulate(vx, vy)
            MAX_Y = max(MAX_Y, r[0])
            if r[0] != -1: 
                valid.append(r[1])
    
    print(f"part 1 ans: {MAX_Y}")
    print(f"part 2 ans: {len(valid)}")
