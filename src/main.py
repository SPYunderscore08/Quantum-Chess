from game import *

def main():
    game = Game()

    game.start()
    game.white.move_piece(8, 1, 3)
    for row in game.board:
        print(row)

if __name__ == '__main__':
    main()