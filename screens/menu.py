# screens/menu.py

from textual.screen import Screen
from textual.widgets import Static, Button
from textual.app import ComposeResult


class MainMenu(Screen):
    """Menú principal del juego."""

    def compose(self) -> ComposeResult:
        yield Static("\n🟩 PUZZLE DESLIZANTE RETRO 🟩\n", classes="title")

        # Selector de dificultad
        yield Button("Puzzle 3×3", id="p3")
        yield Button("Puzzle 4×4", id="p4")
        yield Button("Puzzle 5×5", id="p5")
        # Opciones adicionales
        yield Button("Récords", id="records")
        yield Button("Instrucciones", id="help")
        yield Button("Salir", id="quit")

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id in ("p3", "p4", "p5"):
            from screens.puzzle_screen import PuzzleScreen

            board_size = {"p3": 3, "p4": 4, "p5": 5}[button_id]
            self.app.push_screen(PuzzleScreen(board_size=board_size))

        elif button_id == "help":
            self.app.push_screen("help")

        elif button_id == "quit":
            self.app.exit()

        elif button_id == "records":
            self.app.push_screen("records")
