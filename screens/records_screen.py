# screens/records_screen.py

from textual.screen import Screen
from textual.widgets import Static, Button
from textual.app import ComposeResult

from records import RecordManager


class RecordsScreen(Screen):
    """Pantalla que muestra los récords por dificultad."""

    def __init__(self):
        super().__init__()
        self.record_manager = RecordManager()

    def compose(self) -> ComposeResult:
        yield Static("\n🏆 RÉCORDS DEL PUZZLE 🏆\n", classes="title")

        # Conservamos tu flujo original
        records_text = self._build_records_text()

        # Mejoramos solo el contenedor visual
        yield Static(records_text, classes="records-box")

        yield Button("Volver al menú", id="back", classes="back-button")

    def _build_records_text(self) -> str:
        lines = []

        for size in (3, 4, 5):
            record = self.record_manager.get_record(size)
            best_time = record["best_time"]
            best_moves = record["best_moves"]
            history = record.get("history", [])

            # Añadimos separadores visuales
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append(f"🔷 {size}×{size}")
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            # Récords principales
            time_str = f"{best_time} s" if best_time is not None else "—"
            moves_str = f"{best_moves}" if best_moves is not None else "—"

            lines.append(f"   🥇 Mejor tiempo: {time_str}")
            lines.append(f"   🥇 Mejor movimientos: {moves_str}")

           # Ranking histórico
            if history:
                lines.append("\n   📜 Ranking histórico:")
                for idx, entry in enumerate(history, start=1):
                    t = entry["time"]
                    m = entry["moves"]

                    # Iconos para top 3
                    if idx == 1:
                        icon = "🥇"
                        color = "yellow"
                    elif idx == 2:
                        icon = "🥈"
                        color = "lightgrey"
                    elif idx == 3:
                        icon = "🥉"
                        color = "orange"
                    else:
                        icon = "•"
                        color = "white"

                    lines.append(
                        f"     [bold {color}]{icon} {idx:2}) {t} s – {m} mov[/]")
            else:
                lines.append("\n   📜 Ranking histórico: —")

            lines.append("")  # Espacio entre bloques

        return "\n".join(lines)

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "back":
            self.app.pop_screen()
