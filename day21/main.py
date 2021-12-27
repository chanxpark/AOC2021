class Game(): 
    def __init__(self): 
        self.players = []
        self.player_turn = 0 
        self.dice = 1
        self.rolls = 0 

    def addPlayer(self, player): 
        self.players.append(player)
    
    def getPlayers(self): 
        print(self.players)
    
    def roll(self): 
        steps = 0 
        for _ in range(3): 
            self.rolls += 1 
            steps += self.dice

            # update dice 
            if self.dice == 100: 
                self.dice = 1
            else: 
                self.dice += 1

        # pass to next player 
        self.players[self.player_turn].points(steps)
        # check if win 
        if self.players[self.player_turn].checkWin(): 
            # return losing players score and roll count 
            self.player_turn = 1 if self.player_turn == 0 else 0 
            return (self.players[self.player_turn].getScore(), self.rolls) # score, # wins

        self.player_turn = 1 if self.player_turn == 0 else 0  
        return (-1, -1)

class Player(): 
    def __init__(self, player, pos): 
        self.player = player 
        self.score = 0 
        self.rolls = 0
        self.position = pos
    
    def points(self, steps): 
        c = (self.position + steps) % 10 
        self.position = 10 if c == 0 else c 
        self.score += self.position
        print(f"player {self.player} rolls {steps} and moves to space {self.position} for a total score of {self.score}")
        

    def getScore(self): 
        return self.score
    
    def checkWin(self): 
        return True if self.score >= 1000 else False

if __name__ == "__main__": 
    # set up game
    # start positions 
    # Player 1 starting position: 4
    # Player 2 starting position: 8
    P1 = Player(1, 2)
    P2 = Player(2, 5)
    G = Game()
    G.addPlayer(P1)
    G.addPlayer(P2)
    
    while True: 
        r = G.roll()
        if r[0] != -1: 
            print(f"Player Won: {r} -> {r[0]*r[1]}")
            break
