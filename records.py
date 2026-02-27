# records.py Modulo para manejar los récords de los jugadores
import json
import os


class RecordManager:
    """"
    Gestor de récords para el juego puzzle desliante.
    Administra los récords de los jugadores en un archivo JSON.
    Guarada y carga los tiempos y movimientos por tamaño de tablero.
    """

    FILE_PATH = "records.json"
    MAX_HISTORY = 10  # Número máximo de entradas en el ranking

    def __init__(self):
        self.records = self.load_records()

    # ---------------------------------------------------------
    # CARGA DE ARCHIVO
    # ---------------------------------------------------------
    def load_records(self):
        """Carga los récords desde el archivo JSON."""
        if not os.path.exists(self.FILE_PATH):
            return {}
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    # ---------------------------------------------------------
    # GUARDADO DE ARCHIVO
    # ---------------------------------------------------------
    def save_records(self):
        """Guarda los récords en el archivo JSON."""
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=4, ensure_ascii=False)

    # ---------------------------------------------------------
    # OBTENER RÉCORD
    # ---------------------------------------------------------
    def get_record(self, size):
        """Devuelve el récord para un tamaño dado."""
        size = str(size)

        if size not in self.records:
            # Inicializar con valores por defecto si no existe
            self.records[size] = {
                "best_time": None,
                "best_moves": None,
                "history": []
            }
        return self.records[size]

    # ---------------------------------------------------------
    # COMPROBAR SI ES NUEVO RÉCORD
    # ---------------------------------------------------------
    def is_new_record(self, size, time, moves):
        """Determina si el resultado actual supera el récord existente."""
        record = self.get_record(size)

        is_time_record = (
            record["best_time"] is None or time < record["best_time"]
        )

        is_moves_record = (
            record["best_moves"] is None or moves < record["best_moves"]
        )

        return is_time_record, is_moves_record

    # ---------------------------------------------------------
    # ACTUALIZAR RÉCORD Y RANKING
    # ---------------------------------------------------------
    def update_record(self, size, time, moves):
        """Actualiza el récord y mantiene un ranking ordenado."""
        size = str(size)
        record = self.get_record(size)

        # 1. Añadir la nueva entrada al historial
        history_entry = {"time": time, "moves": moves}
        record["history"].append(history_entry)

        # 2. Ordenar el historial por tiempo ascendente, luego por movimientos ascendentes
        record["history"].sort(key=lambda x: (x["time"], x["moves"]))

        # 3. Limitar a top N (MAX_HISTORY)
        record["history"] = record["history"][:self.MAX_HISTORY]

        # 4. Actualizar récords principales según el nuevo top 1
        best = record["history"][0]
        record["best_time"] = best["time"]
        record["best_moves"] = best["moves"]

        # 5. Guardar cambios
        self.records[size] = record
        self.save_records()

    # ---------------------------------------------------------
    # OBTENER RANKING
    # ---------------------------------------------------------
    def get_history(self, size):
        return self.get_record(size).get("history", [])
