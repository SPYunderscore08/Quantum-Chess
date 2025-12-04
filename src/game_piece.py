from enum import Enum

class Piece:
    id:int
    x:int
    y:int

    def __init__(self, piece_id:int, x:int, y:int):
        self.id = piece_id
        self.x = x
        self.y = y

    def move(self, x:int, y:int):
        self.x = x
        self.y = y


class Pawn(Piece):
    class Moves(Enum):
        FORWARDS = 0
        DIAGONAL_LEFT = 1
        DIAGONAL_RIGHT = 2

    def move(self, x:int, y:int):
        pass

    def en_passant(self, x:int, y:int):
        pass

    def promote(self, x:int): # todo might pass new piece directly
        pass

class Knight(Piece):
    def move(self, x:int, y:int):
        pass


class Bishop(Piece):
    class Moves(Enum):
        DIAGONAL_LEFT_UP = 0
        DIAGONAL_LEFT_DOWN = 1
        DIAGONAL_RIGHT_UP = 2
        DIAGONAL_RIGHT_DOWN = 3

    def move(self, x:int, y:int):
        pass

class Rook(Piece):
    class Moves(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    def move(self, x:int, y:int):
        pass

    def castle(self, x:int, y:int):
        pass

class Queen(Piece):
    class Moves(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3
        DIAGONAL_LEFT_UP = 4
        DIAGONAL_LEFT_DOWN = 5
        DIAGONAL_RIGHT_UP = 6
        DIAGONAL_RIGHT_DOWN = 7

    def move(self, x:int, y:int):
        pass


class King(Piece):
    class Moves(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3
        DIAGONAL_LEFT_UP = 4
        DIAGONAL_LEFT_DOWN = 5
        DIAGONAL_RIGHT_UP = 6
        DIAGONAL_RIGHT_DOWN = 7

    def move(self, x:int, y:int):
        pass
