from puzzle import Puzzle3x3
from utils.display import Display


def main():
    """
    Función principal del programa.
    Inicia una partida del rompecabezas 3x3, muestra el tablero inicial
    y permite al usuario mover las piezas mediante comandos de texto.

    El bucle principal continúa hasta que el usuario escriba 'exit'.
    Cada movimiento válido actualiza y muestra el tablero.
    """
    ui = Display(colored=True)
    game = Puzzle3x3()          # Crea una nueva instancia del rompecabezas
    ui.show_board(game.board)   # Muestra el tablero inicial

    while True:
        # Solicita al usuario una dirección de movimiento
        move = input("Mover (up/down/left/right) o 'exit': ").strip().lower()

        if move == 'exit':
            print("¡Gracias por jugar!")
            break

        # Intenta realizar el movimiento solicitado
        if game.move(move):
            ui.show_board(game.board)  # Muestra el tablero actualizado
        else:
            ui.show_title()
            ui.show_message("Movimiento inválido", color=Colors.YELLOW)


if __name__ == "__main__":
    main()
