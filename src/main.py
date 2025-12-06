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

    game.white.move_piece(8, 2, 7)
    game.print_board()

    game.white.move_piece(8, 1, 8)
    game.print_board()




if __name__ == '__main__':
    main()