from puzzle import Puzzle3x3
from utils.display import display_board


def main():
    game = Puzzle3x3()
    display_board(game.board)

    while True:
        move = input("Mover (up/down/left/right) o 'exit': ").strip().lower()
        if move == 'exit':
            print("¡Gracias por jugar!")
            break
        if game.move(move):
            display_board(game.board)
        else:
            print("Movimiento inválido. Intenta otra dirección.")


if __name__ == "__main__":
    main()
