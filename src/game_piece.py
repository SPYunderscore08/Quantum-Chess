from numpy.f2py.auxfuncs import throw_error


class Piece:
    piece_id:int
    x:int
    y:int

    def __init__(self, piece_id:int, x:int, y:int):
        self.piece_id = piece_id
        self.x = x
        self.y = y

    def move(self, x:int, y:int):
        pass

    def check_validity(self, x:int, y:int):
        return True

class Pawn(Piece):
    def move(self, x: int, y: int):
        super().move(x, y)
        self.check_validity()

    def promote(self, x:int): # todo might pass new piece directly
        pass

class Knight(Piece):
    def move(self, x:int, y:int):
        pass

class Bishop(Piece):
    def move(self, x:int, y:int):
        pass

class Rook(Piece):
    def move(self, x:int, y:int):
        pass

class Queen(Piece):
    def move(self, x:int, y:int):
        pass

class King(Piece):
    def move(self, x:int, y:int):
        pass
