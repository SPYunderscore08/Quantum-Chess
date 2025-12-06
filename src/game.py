from player import Player
from game_piece import *

class Game:
    board:list
    side:bool

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] # It's not going to be checkers!
        self.initialize_game_pieces()
        self.white = Player(self.board)
        self.black = Player(self.board)
        self.side = True


    def initialize_game_pieces(self): # Generated
        back_rank_order = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        id_running: int = 0

        # White back rank (row 0)
        for column, piece_type in enumerate(back_rank_order):
            piece_class = globals()[piece_type]
            self.board[0][column] = piece_class(id_running, column + 1, 1, True, self.board)
            id_running += 1

        # White pawns (row 1)
        for column in range(8):
            self.board[1][column] = Pawn(id_running, column + 1, 2, True, self.board)
            id_running += 1

        # Black pawns (row 6)
        for column in range(8):
            self.board[6][column] = Pawn(id_running, column + 1, 7, False, self.board)
            id_running += 1

        # Black back rank (row 7) - same order
        for column, piece_type in enumerate(back_rank_order):
            piece_class = globals()[piece_type]
            self.board[7][column] = piece_class(id_running, column + 1, 8, False, self.board)
            id_running += 1


    def start(self):
        self.side = True


    def print_board(self):
        print("-" * 23)
        for row in self.board:
            for item in row:
                print((type(item)).__name__[:2] + str(item.piece_id), end=" ") if not item == None else print(" ", end=" ")
            print("|")
        print("-" * 23)
#