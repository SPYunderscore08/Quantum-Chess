from enum import Enum

class Piece:
    id = 0
    x = 0
    y = 0

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Pawn(Piece):
    class Moves(Enum):
        FORWARDS = 0
        DIAGONAL_LEFT = 1
        DIAGONAL_RIGHT = 2

    def move(self, x, y):
        pass

    def promote(self, x, ):