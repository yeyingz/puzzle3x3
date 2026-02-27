# screens/puzzle_screen.py

from textual.widgets import Static, Button
from textual.screen import Screen
from textual.reactive import reactive
from textual.app import ComposeResult

from puzzle import Puzzle3x3, Puzzle4x4, Puzzle5x5
from textual.geometry import Offset

from records import RecordManager


class PuzzleWidget(Static):
    """Widget que muestra el tablero del puzzle en formato texto."""

    board = reactive([])

    def on_mount(self):
        # Posición inicial sin desplazamiento
        self.styles.offset = Offset(0, 0)

    def animate_move(self, direction: str):
        """Animación suave según la dirección del movimiento."""
        dx, dy = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }[direction]

        # Desplazamiento pequeño
        offset_x = dx * 2
        offset_y = dy * 1

        # Ida
        self.animate("offset", Offset(offset_x, offset_y), duration=0.08)
        # Vuelta
        self.animate("offset", Offset(0, 0), duration=0.08, delay=0.08)

    def render(self):
        lines = []
        for row in self.board:
            line = " | ".join(
                str(c).rjust(2) if c != " " else "⬜" for c in row
            )
            lines.append(line)
        return "\n".join(lines)


class StatsWidget(Static):
    """Panel lateral con estadísticas del juego."""

    moves = reactive(0)
    time = reactive(0)

    def compose(self):
        # Título de estadísticas
        yield Static("📊 ESTADÍSTICAS\n")
        # Etiquetas para mostrar movimientos y tiempo
        self.moves_label = Static()
        self.time_label = Static()
        # Agregar las etiquetas al layout
        yield self.moves_label
        yield self.time_label
        # Botón de reinicio
        yield Button("Reiniciar", id="reset")

    def watch_moves(self, moves):
        if hasattr(self, "moves_label"):
            self.moves_label.update(f"Movimientos: {moves}")

    def watch_time(self, time):
        if hasattr(self, "time_label"):
            minutes = time // 60
            seconds = time % 60
            self.time_label.update(f"Tiempo: {minutes:02d}:{seconds:02d}")


class VictoryWidget(Static):
    """Widget que se muestra cuando el jugador resuelve el puzzle."""

    def render(self):
        return (
            "\n🎉 ¡PUZZLE COMPLETADO! 🎉\n\n"
            "Pulsa ESC para volver al menú\n"
        )


class PuzzleScreen(Screen):
    """Pantalla de juego del puzzle deslizante 3x3."""

    solved = reactive(False)

    def __init__(self, board_size: int = 3):
        super().__init__()
        self.board_size = board_size
        if board_size == 3:
            self.game = Puzzle3x3()
        elif board_size == 4:
            self.game = Puzzle4x4()
        elif board_size == 5:
            self.game = Puzzle5x5()
        else:
            raise ValueError(f"Tamaño de puzzle no soportado: {size}")

        self.move_count = 0
        self.time_elapsed = 0

        self.records = RecordManager()

    def compose(self) -> ComposeResult:
        # Widget principal del tablero
        self.puzzle_widget = PuzzleWidget()
        self.puzzle_widget.board = self.game.board
        # Widget lateral de estadísticas
        self.stats_widget = StatsWidget()
        # Layout horizontal con el tablero a la izquierda y estadísticas a la derecha
        yield self.puzzle_widget
        yield self.stats_widget

    def on_mount(self):
        # Temporizador que se ejecuta cada segundo
        self.set_interval(1, self.update_timer)
        self.stats_widget.moves = 0
        self.stats_widget.time = 0

    def update_timer(self):
        # Solo actualizar el tiempo si el puzzle no está resuelto
        if not self.solved:
            self.time_elapsed += 1
            self.stats_widget.time = self.time_elapsed

    def reset_game(self):
        """Reinicia el estado completo del puzzle."""
        # Crear un nuevo puzzle
        if self.board_size == 3:
            self.game = Puzzle3x3()
        elif self.board_size == 4:
            self.game = Puzzle4x4()
        elif self.board_size == 5:
            self.game = Puzzle5x5()

        # Resetear contadores
        self.move_count = 0
        self.time_elapsed = 0
        self.solved = False

        # Actualizar el tablero (copia profunda para activar reactividad)
        self.puzzle_widget.board = [row[:] for row in self.game.board]
        self.puzzle_widget.refresh(layout=True)

        # Resetear estadísticas visibles
        self.stats_widget.moves = 0
        self.stats_widget.time = 0

        # Sonido suave de reinicio
        self.app.bell()

    def on_button_pressed(self, event):
        """Detecta pulsación de botones dentro de la pantalla."""
        if event.button.id == "reset":
            self.reset_game()

    def show_victory(self):
        """Marca el puzzle como resuelto y muestra el mensaje de victoria."""
        self.solved = True

        # --- COMPROBAR RÉCORDS ---
        is_time_record, is_moves_record = self.records.is_new_record(
            self.board_size,
            self.time_elapsed,
            self.move_count
        )

        # if is_time_record or is_moves_record:
        self.records.update_record(
            self.board_size,
            self.time_elapsed,
            self.move_count
        )

        # --- MOSTRAR MENSAJE DE VICTORIA ---
        self.mount(VictoryWidget())

        # Sonidos
        self.app.bell()
        self.set_timer(0.1, self.app.bell)
        self.set_timer(0.2, self.app.bell)

        # --- MENSAJE OPCIONAL DE RÉCORD ---
        if is_time_record or is_moves_record:
            msg = "\n🏆 ¡Nuevo récord!\n"
            if is_time_record:
                msg += f"⏱️ Tiempo: {self.time_elapsed} segundos\n"
            if is_moves_record:
                msg += f"🔢 Movimientos: {self.move_count}\n"

            self.mount(Static(msg, classes="record-message"))

    def on_key(self, event):
        key = event.key

        # Volver al menú con ESC
        if key == "escape":
            self.app.pop_screen()
            return

        # Si ya está resuelto, ignorar más movimientos
        if self.solved:
            return

        moves = {
            "up": "up",
            "down": "down",
            "left": "left",
            "right": "right",
        }

        if key in moves:
            moved = self.game.move(moves[key])
            if moved:
                self.move_count += 1
                self.stats_widget.moves = self.move_count

                # self.puzzle_widget.board = self.game.board
                self.puzzle_widget.board = [row[:] for row in self.game.board]
                self.puzzle_widget.refresh(layout=True)
                self.puzzle_widget.animate_move(moves[key])
                self.app.bell()  # Sonido de movimiento
                if self.game.is_solved():
                    self.show_victory()
            else:
                self.app.bell()  # Sonido de error si el movimiento no es válido
                # Sonido de error adicional para mayor feedback
                self.set_timer(0.05, self.app.bell)
