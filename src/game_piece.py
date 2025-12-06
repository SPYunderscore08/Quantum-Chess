class Piece:
    def __init__(self, piece_id:int, x:int, y:int, side:bool, board:list):
        self.piece_id = piece_id
        self.x = x
        self.y = y
        self.side = side
        self.board = board

    def move(self, x:int, y:int):
        if self.check_validity(x, y):
            self.board[y][x] = self
            self.board[self.y][self.x] = "None"
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
            if not self.is_valid_coordinate(x, y):
                print("Invalid Coordinate")
                return False
            elif self.puts_king_in_check(x, y):
                print("Puts King in Check")
                return False
            elif self.path_blocked(x, y):
                print("Path is Blocked")
                return False

            return True
        else:
            if not self.is_valid_coordinate(x, y):
                print("Invalid Coordinate")
                return False
            elif self.puts_king_in_check(x, y):
                print("Puts King in Check")
                return False
            elif self.path_blocked(x, y):
                print("Path is Blocked")
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
            return self.can_capture(x, y)

        return True

    def puts_king_in_check(self, x:int, y:int):
        pass # todo actually check state of game/state
        return False

    def path_blocked(self, x:int, y:int):
        """path:list = [
            Game.board[self.y + 1][self.x],
            Game.board[self.y + 2][self.x]
        ]"""

        for i in range(self.x, x - self.x):
            if issubclass(type(self.board[y][i]), Piece):
                return True

        return False

    def can_capture(self, x:int, y:int):
        return True if issubclass(type(self.board[y][x]), Piece) else False

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
