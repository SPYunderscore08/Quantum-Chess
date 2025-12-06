from game import *

def main():
    game = Game()

    game.start()

    game.white.move_piece(8, 1, 3)
    game.print_board()

    game.white.move_piece(8, 1, 4)
    game.print_board()

    game.white.move_piece(8, 1, 5)
    game.print_board()

    game.white.move_piece(8, 1, 6)
    game.print_board()

    item = Pawn(255, 3, 6, True, game.board)
    item.is_en_passant_able = True
    game.board[5][1] = item
    game.board[6][1] = None
    game.print_board()

    game.white.move_piece(8, 2, 7)
    game.print_board()
    game.white.move_piece(8, 1, 8)
    game.print_board()


    game.black.move_piece(23, 8, 5)
    game.print_board()

    game.black.move_piece(23, 8, 4)
    game.print_board()

    game.black.move_piece(23, 8, 3)
    game.print_board()

    game.black.move_piece(23, 7, 2)
    game.print_board()

    game.black.move_piece(23, 6, 1)
    game.print_board()


if __name__ == '__main__':
    main()