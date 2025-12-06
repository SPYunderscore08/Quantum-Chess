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

    game.white.move_piece(8, 2, 7)
    game.print_board()


    game.print_board()

    #game.





if __name__ == '__main__':
    main()