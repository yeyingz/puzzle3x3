# screens/help.py

from textual.screen import Screen
from textual.widgets import Static
from textual.app import ComposeResult


class HelpScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Static(
            "\n📘 INSTRUCCIONES\n\n"
            "El objetivo del puzzle es ordenar las fichas del 1 al 8\n"
            "dejando el espacio vacío al final.\n\n"
            "Usa las flechas del teclado para mover las fichas.\n"
            "Pulsa ESC para volver al menú.\n"
        )

    def on_key(self, event):
        if event.key == "escape":
            self.app.pop_screen()
