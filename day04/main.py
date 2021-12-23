from typing import List, Sized, Tuple
from collections import namedtuple

class Bingo: 
    def __init__(self, board): 
        self.board: List[List[int]] = board
        self.won: bool = False 
        self.marks: List[Tuple[int, int]] = [] # coordinates of marks (row, col)

    # checks to see if mark is on board and adds coordinates to marks
    def add_mark(self, mark: int) -> None: 
        for i, v in enumerate(self.board): 
            if mark in v:
                self.marks.append((i, v.index(mark))) 

    def check_win(self) -> bool: 
        size = 5 # bingo board size

        
        for n in range(size): 
        # check columns
            for row in range(size): 
                # if coordinates not in marks; go to next col
                if (row, n) not in self.marks: 
                    break
                # if entire column is in marks; return true 
                if row == size - 1: 
                    self.won = True 
                    return True

        # check rows
            for col in range(size): 
                # if coordinates not in marks; go to next row 
                if (n, col) not in self.marks: 
                    break
                # if entire row is in marks; return true 
                if col == size - 1: 
                    self.won = True 
                    return True

        # if no row or col is found; return false 
        return False

class Game: 
    def __init__(self): 
        self.games: List[Bingo] = []
        self.last_won_board: Bingo = None # the last winning board
        self.last_draw: int = 0 
        self.num_games: int = 0 # counts the number of boards in play 
        self.num_won_boards: int = 0 # counts the number of boards that have won 

    def add_board(self, board: Bingo) -> None: 
        self.games.append(board)
        self.num_games += 1 

    # adds draw; returns true if a board has won else false
    def draw(self, number: int) -> None: 
        self.last_draw = number
        for game in self.games: 
            if not game.won:
                game.add_mark(number)

                if game.check_win(): 
                    self.last_won_board = game
                    self.num_won_boards += 1
    
    def calculate_win(self) -> int: 
        result = 0
        for row_i, row_v in enumerate(self.last_won_board.board): 
            for col_i, col_v in enumerate(row_v): 
                if (row_i, col_i) not in self.last_won_board.marks:
                    result += col_v
        return result * self.last_draw

def play_game(boards, draws) -> int: 

    # initiate games
    bingo_game = Game()

    for board in boards: 
        bingo_game.add_board(Bingo(board))

    # go through draws until all boards have won 
    for draw in draws: 
        print(draw)
        bingo_game.draw(draw)
        if bingo_game.num_games == bingo_game.num_won_boards: 
            break

    return bingo_game.calculate_win()

# format board into 2d matrix
def format_board(board: str) -> List[List[int]]: 
    rows: List[str] = board.strip().split("\n")
    formatted_board: List[List[str]] = []
    for row in rows: 
        formatted_board.append([ int(val) for val in row.strip().split() ])

    return formatted_board

if __name__ == "__main__": 
    f = "input.txt"
    # separate draws and boards from stdin 
    with open(f, "r") as input: 
        line_breaks: List[str] = input.read().strip().split("\n\n")

    draws: List[int] = [ int(n) for n in line_breaks[0].strip().split(",") ]
    boards: List[List[int]] = [ format_board(board) for board in line_breaks[1:] ]

    print(play_game(boards, draws))