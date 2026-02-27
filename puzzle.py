# puzzle.py
import random


class BasePuzzle:
    """
    Clase base para puzzles deslizantes NxN.
    Contiene toda la lógica común para cualquier tamaño.
    """

    def __init__(self, size: int):
        self.size = size
        self.board = self.generate_board()

    # ---------------------------------------------------------
    # GENERACIÓN DEL TABLERO
    # ---------------------------------------------------------
    def generate_board(self):
        """
        Genera un tablero NxN con números del 1 al N*N-1 y un espacio vacío.
        Mezcla aleatoriamente los valores.
        """
        total = self.size * self.size
        numbers = list(range(1, total)) + [" "]
        random.shuffle(numbers)

        # Convertir a matriz NxN
        return [numbers[i:i + self.size] for i in range(0, total, self.size)]

    # ---------------------------------------------------------
    # BÚSQUEDA DEL ESPACIO VACÍO
    # ---------------------------------------------------------
    def find_empty(self):
        """
        Devuelve la posición (fila, columna) del espacio vacío.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    return i, j

    # ---------------------------------------------------------
    # MOVIMIENTO
    # ---------------------------------------------------------
    def move(self, direction: str):
        """
        Intenta mover el espacio vacío en la dirección indicada.
        Devuelve True si el movimiento es válido.
        """
        x, y = self.find_empty()

        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        dx, dy = moves.get(direction, (0, 0))
        new_x = x + dx
        new_y = y + dy

        # Validar límites
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            # Intercambiar
            self.board[x][y], self.board[new_x][new_y] = \
                self.board[new_x][new_y], self.board[x][y]
            return True

        return False

    # ---------------------------------------------------------
    # ESTADO DE VICTORIA
    # ---------------------------------------------------------
    def is_solved(self):
        """
        Verifica si el tablero está en el estado de victoria:
        1 2 3 ... N
        ...
        N*N-1 ' '
        """
        total = self.size * self.size
        solved = list(range(1, total)) + [" "]
        flat = [cell for row in self.board for cell in row]
        return flat == solved


# ============================================================
# CLASES ESPECÍFICAS (3×3, 4×4, 5×5)
# ============================================================

class Puzzle3x3(BasePuzzle):
    def __init__(self):
        super().__init__(size=3)


class Puzzle4x4(BasePuzzle):
    def __init__(self):
        super().__init__(size=4)


class Puzzle5x5(BasePuzzle):
    def __init__(self):
        super().__init__(size=5)
