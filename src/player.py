from game_piece import *

class Player:
    def __init__(self, board:list):
        self.board = board

    def move_piece(self, piece_id:int, x:int, y:int): # todo
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if issubclass(type(self.board[i][j]), Piece):
                    if self.board[i][j].piece_id == piece_id:
                        print(type(self.board[i][j]))
                        self.board[i][j].move(x, y)
                        return