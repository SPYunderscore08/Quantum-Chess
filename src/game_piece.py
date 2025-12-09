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

    def check_validity(self, x:int, y:int) -> bool:
        return True

    def puts_king_in_check(self, x:int, y:int) -> bool:
        pass # todo actually check state of game/state
        return False

    def path_blocked(self, x: int, y: int) -> bool:
        return False

class Pawn(Piece):
    is_en_passant_able:bool = False
    does_en_passant:bool = False

    def move(self, x:int, y:int):
        if self.check_validity(x, y):
            self.board[y - 1][x - 1] = self
            if self.does_en_passant:
                self.board[(y - 2) if self.side else (y + 1)][x - 1] = None
                self.does_en_passant = False

            self.board[self.y - 1][self.x - 1] = None

            self.x = x
            self.y = y
            if self.y == 8 if self.side else 1:
                self.promote()
        else:
            raise Exception("Invalid Move!")

    def check_validity(self, x:int, y:int) -> bool:
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
            if self.path_blocked(x, y):
                print("Path is Blocked")
                return False

        if self.puts_king_in_check(x, y):
            print("Puts King in Check")
            return False

        return True


    def is_valid_coordinate(self, x:int, y:int) -> bool:
        if x == self.x and y == self.y:  # todo might get changed; depending on if splitting allows this
            return False  # Cannot put piece where piece stood

        if self.side:
            if y <= self.y:
                return False
        else:
            if y >= self.y:
                return False

        if (x < 1 or x > 8) or (y < 1 or y > 8):
            return False # Out of bounds

        elif not (abs(y - self.y) == 1 or (abs(y - self.y) == 2 and self.y == (2 if self.side else 7))):
            return False

        elif abs(self.x - x) > 1:
            return False

        self.is_en_passant_able = False
        if abs(y - self.y) == 2 and self.y == (2 if self.side else 7):
            self.is_en_passant_able = True

        return True


    def path_blocked(self, x:int, y:int) -> bool:
        """path:list = [
            Game.board[self.y + 1][self.x],
            Game.board[self.y + 2][self.x]
        ]"""
        if self.side:
            for i in range(self.y, y):
                if issubclass(type(self.board[i][x - 1]), Piece):
                    return True

        else: # JANK
            for i in range(self.y, y, -1):
                if issubclass(type(self.board[i - 2][x - 1]), Piece):
                    return True

        return False

    def can_capture(self, x:int, y:int) -> bool:
        if issubclass(type(self.board[y - 1][x - 1]), Piece) and self.board[y - 1][x - 1].side != self.side and abs(self.x - x) == 1:
            return True

        elif type(self.board[(y - 2) if self.side else (y + 1)][x - 1]) == Pawn and self.board[(y - 2) if self.side else (y + 1)][x - 1].is_en_passant_able:
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
    def check_validity(self, x: int, y: int) -> bool:
        """
        """
        if not self.is_valid_coordinate(x, y):
            print("Invalid Coordinate")
            return False

        elif self.path_blocked(x, y):
            if not self.can_capture(x, y):
                print("Cannot capture own pieces")
                return False

        if self.puts_king_in_check(x, y):
            print("Puts King in Check")
            return False

        return True

    def is_valid_coordinate(self, x: int, y: int):
        if x == self.x and y == self.y:
            return False

        elif (x < 1 or x > 8) or (y < 1 or y > 8):
            return False  # Out of bounds

        elif (abs(self.x - x) > 1 or abs(self.y - y) > 1) and (not self.can_castle(x, y)): # todo might be changed
            return False

        return True

    def path_blocked(self, x: int, y: int) -> bool:
        if issubclass(type(self.board[y - 1][x - 1]), Piece):
            return True
        return False

    def can_capture(self, x:int, y:int) -> bool:
        if self.board[y - 1][x - 1].side != self.side:
            return True
        return False

    def can_castle(self, x, y):
        pass
