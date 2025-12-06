from game_piece import *

class Board:
    board:list

    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] # It's not going to be checkers!
        self.initialize_game_pieces()

    def initialize_game_pieces(self): # Generated
        back_rank_order = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        id_running: int = 0

        # White back rank (row 0)
        for column, piece_type in enumerate(back_rank_order):
            piece_class = globals()[piece_type]
            self.board[0][column] = piece_class(id_running, column + 1, 1)
            id_running += 1

        # White pawns (row 1)
        for column in range(8):
            self.board[1][column] = Pawn(id_running, column + 1, 2)
            id_running += 1

        # Black pawns (row 6)
        for column in range(8):
            self.board[6][column] = Pawn(id_running, column + 1, 7)
            id_running += 1

        # Black back rank (row 7) - same order
        for column, piece_type in enumerate(back_rank_order):
            piece_class = globals()[piece_type]
            self.board[7][column] = piece_class(id_running, column + 1, 8)
            id_running += 1

        print(self.board)

    def start_game(self):
        pass