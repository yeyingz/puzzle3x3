import random


class Puzzle3x3:
    """
    Clase que representa un rompecabezas deslizante de 3x3 (8-puzzle).
    El tablero contiene los números del 1 al 8 y un espacio vacío que
    puede moverse en cuatro direcciones si es posible.
    """

    def __init__(self):
        """
        Constructor de la clase.
        Inicializa el tablero generando una configuración aleatoria.
        """
        self.board = self.generate_board()

    def generate_board(self):
        """
        Genera un tablero aleatorio de 3x3 con los números del 1 al 8
        y un espacio vacío representado por ' '.

        Returns:
            list[list]: Matriz 3x3 representando el tablero.
        """
        numbers = list(range(1, 9)) + [' ']  # Crea la lista [1..8, ' ']
        random.shuffle(numbers)              # Mezcla los elementos
        # Convierte la lista en una matriz 3x3
        return [numbers[i:i+3] for i in range(0, 9, 3)]

    def find_empty(self):
        """
        Busca la posición del espacio vacío dentro del tablero.

        Returns:
            tuple: Coordenadas (fila, columna) del espacio vacío.
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return i, j

    def move(self, direction):
        """
        Intenta mover el espacio vacío en la dirección indicada.

        Args:
            direction (str): Dirección del movimiento. Puede ser:
                             'up', 'down', 'left', 'right'.

        Returns:
            bool: True si el movimiento fue válido y se realizó,
                  False si no fue posible.
        """
        x, y = self.find_empty()  # Posición actual del espacio vacío

        moves = {
            'up':    (-1, 0),
            'down':  (1, 0),
            'left':  (0, -1),
            'right': (0, 1)
        }

        # Diccionario que define el desplazamiento según la dirección
        dx, dy = moves.get(direction, (0, 0))

        # Calcula la nueva posición dependiendo del tipo de movimiento
        new_x = x + dx
        new_y = y + dy

        # Verifica que la nueva posición esté dentro del tablero
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Intercambia el espacio vacío con la casilla destino
            self.board[x][y], self.board[new_x][new_y] = \
                self.board[new_x][new_y], self.board[x][y]
            return True

        return False
