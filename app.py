# app.py

from textual.app import App

from screens.menu import MainMenu
from screens.puzzle_screen import PuzzleScreen
from screens.help import HelpScreen
from screens.records_screen import RecordsScreen


class PuzzleApp(App):

    CSS_PATH = "app.css"  # Archivo CSS para estilos

    def on_mount(self):
        self.install_screen(MainMenu(), name="menu")
        self.install_screen(PuzzleScreen(), name="puzzle")
        self.install_screen(HelpScreen(), name="help")
        self.install_screen(RecordsScreen(), name="records")
        # Pantalla inicial
        self.push_screen("menu")


if __name__ == "__main__":
    PuzzleApp().run()
