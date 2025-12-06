class Piece:
    def __init__(self, piece_id:int, x:int, y:int, side:bool, board:list):
        self.piece_id = piece_id
        self.x = x
        self.y = y
        self.side = side
        self.board = board

    def move(self, x:int, y:int):
        if self.check_validity(x, y):
            self.board[y - 1][x - 1] = self
            self.board[self.y - 1][self.x - 1] = None
            self.x = x
            self.y = y
        else:
            raise Exception("Invalid Move!")

    def check_validity(self, x:int, y:int):
        return True

class Pawn(Piece):
    is_en_passant_able:bool = False
    does_en_passant:bool = False

    def move(self, x:int, y:int):
        if self.check_validity(x, y):
            self.board[y - 1][x - 1] = self
            if self.does_en_passant:
                self.board[y - 2][x - 1] = None
                self.does_en_passant = False
            self.board[self.y - 1][self.x - 1] = None
            self.x = x
            self.y = y
            if self.y == 8:
                self.promote()
        else:
            raise Exception("Invalid Move!")

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
            elif not self.can_capture(x, y):
                if self.puts_king_in_check(x, y):
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
            elif not self.can_capture(x, y):
                if self.puts_king_in_check(x, y):
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

        self.is_en_passant_able = False
        if y - self.y == 2 and self.y == 2:
            self.is_en_passant_able = True

        return True

    def puts_king_in_check(self, x:int, y:int):
        pass # todo actually check state of game/state
        return False

    def path_blocked(self, x:int, y:int):
        """path:list = [
            Game.board[self.y + 1][self.x],
            Game.board[self.y + 2][self.x]
        ]"""
        for i in range(self.y, y):
            if issubclass(type(self.board[i][x]), Piece):
                return True

        return False

    def can_capture(self, x:int, y:int):
        if issubclass(type(self.board[y - 1][x - 1]), Piece) and abs(self.x - x) == 1:
            return True
        elif type(self.board[y - 2][x - 1]) == Pawn and self.board[y - 2][x - 1].is_en_passant_able:
            self.does_en_passant = True
            return True
        return False

    def promote(self): # todo might pass new piece directly
        print("Please Promote")


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
