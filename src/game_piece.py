from game import *

class Piece:
    def __init__(self, piece_id:int, x:int, y:int, side:bool):
        self.piece_id = piece_id
        self.x = x
        self.y = y
        self.side = side

    def move(self, x:int, y:int):
        if self.check_validity(x, y):
            self.x = x
            self.y = y
        else:
            raise Exception("Invalid Move!")

    def check_validity(self, x:int, y:int):
        return True

class Pawn(Piece):
    def check_validity(self, x:int, y:int):
        if self.side:
            """
                if out of range of moves
                    if pawn at square 2
                    else raise/false
                if puts king into check
                if piece where coords
                    if valid capture
                    else raise/false
            """
            return True
        else:
            if not self.is_valid_coordinate(x, y):
                return False
            elif self.puts_king_in_check(x, y):
                return False
            elif self.path_blocked(x, y):
                return False

            return True

    def is_valid_coordinate(self, x:int, y:int):
        if x == self.x and y == self.y:  # todo might get changed; depending on if splitting allows this
            return False  # Cannot put piece where piece stood

        elif (x < 1 or x > 8) or (y < 1 or y > 8):
            return False # Out of bounds

        elif not (y - self.y == 1 or (y - self.y == 2 and self.y == 2)): # todo might be wrong
            return False

        elif x != self.x:
            return self.can_capture()

        return True

    def puts_king_in_check(self, x:int, y:int):
        pass # todo actually check state of game/state
        return False

    def path_blocked(self, x:int, y:int):
        path:list = [
            Game.board[self.y + 1][self.x],
            Game.board[self.y + 2][self.x]
        ]

        for i in range(self.x, x - self.x):
            if issubclass(Game.board[y][i], Piece):
                return True

        return False

    def can_capture

    def promote(self, x:int): # todo might pass new piece directly
        pass

class Knight(Piece):
    def check_validity(self, x:int, y:int) -> bool:
        pass

class Bishop(Piece):
    def check_validity(self, x:int, y:int) -> bool:
        pass

class Rook(Piece):
    def check_validity(self, x:int, y:int) -> bool:
        pass

class Queen(Piece):
    def check_validity(self, x:int, y:int) -> bool:
        pass

class King(Piece):
    def check_validity(self, x:int, y:int) -> bool:
        pass
