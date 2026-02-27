# utils/display.py

class Colors:
    """Colores ANSI para mejorar la visualización del tablero."""
    RESET = "\033[0m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"


class Display:
    """
    Clase encargada de mostrar el tablero y gestionar la interfaz visual.
    Permite elegir entre modo simple o modo coloreado.
    """

    def __init__(self, colored=False):
        """
        Args:
            colored (bool): Si True, usa colores ANSI.
        """
        self.colored = colored

    # ---------------------------------------------------------
    # TÍTULO
    # ---------------------------------------------------------
    def show_title(self):
        print(
            f"{Colors.BOLD}{Colors.CYAN}\n=== PUZZLE DESLIZANTE 3x3 ==={Colors.RESET}\n")

    # ---------------------------------------------------------
    # TABLERO
    # ---------------------------------------------------------
    def show_board(self, board):
        """
        Muestra el tablero usando el modo seleccionado.
        """
        if self.colored:
            self._show_board_colored(board)
        else:
            self._show_board_simple(board)

    def _show_board_simple(self, board):
        """Versión sin colores."""
        print("\nRompecabezas 3x3:\n")
        for row in board:
            print(" | ".join(str(cell).rjust(2) for cell in row))
        print()

    def _show_board_colored(self, board):
        """Versión con colores."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}Rompecabezas 3x3:{Colors.RESET}\n")

        for row in board:
            formatted_row = []
            for cell in row:
                if cell == " ":
                    colored = f"{Colors.YELLOW}⬜{Colors.RESET}"
                else:
                    colored = f"{Colors.GREEN}{str(cell).rjust(2)}{Colors.RESET}"
                formatted_row.append(colored)

            print(" | ".join(formatted_row))

        print()

    # ---------------------------------------------------------
    # MENSAJES
    # ---------------------------------------------------------
    def show_message(self, msg, color=Colors.CYAN):
        print(f"{color}{msg}{Colors.RESET}")
