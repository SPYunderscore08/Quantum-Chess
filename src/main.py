from game import *

def main():
    game = Game()

    game.start()
    """
    game.white.move_piece(8, 1, 3)
    game.print_board()

    game.white.move_piece(8, 1, 4)
    game.print_board()

    game.white.move_piece(8, 1, 5)

    game.black.move_piece(17, 2, 5)
    game.print_board()

    print(game.black.board[4][1].is_en_passant_able)
    game.white.move_piece(8, 2, 6)
    game.print_board()

    game.white.move_piece(8, 1, 7)
    game.print_board()

    game.white.move_piece(8, 2, 8)
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

    game.black.move_piece(20, 5, 5)
    game.print_board()

    game.black.move_piece(28, 5, 7)
    game.print_board()

    game.black.move_piece(28, 5, 6)
    game.print_board()

    game.black.move_piece(28, 4, 5)
    game.print_board()

    game.black.move_piece(28, 5, 4)
    game.print_board()
    """

    game.white.move_piece(8, 1, 4)
    game.white.move_piece(8, 1, 5)
    #game.white.move_piece(8, 1, 6)
    game.print_board()

    game.black.move_piece(17, 2, 5)
    game.print_board()

    game.white.move_piece(8, 2, 6)
    game.print_board()


if __name__ == '__main__':
    main()