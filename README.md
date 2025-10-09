# 🧩 Rompecabezas 3x3 en Python

Rompecabezas 3x3 en Python Este proyecto recrea el clásico juego de rompecabezas deslizante 3x3, desarrollado originalmente en Visual Basic y ahora modernizado con Python. Incluye una versión en consola y una interfaz gráfica con Tkinter.

El objetivo es ordenar las fichas del 1 al 8 dejando el espacio vacío en la esquina inferior derecha, moviendo solo fichas adyacentes al espacio libre (Este proyecto demuestra habilidades en lógica algorítmica, estructuras de datos, programación orientada a objetos y diseño de interfaces gráficas).

- 🎮 **Consola**: Usa comandos de texto para mover las fichas.
- 🖱️ **Interfaz gráfica (Tkinter)**: Haz clic en las fichas para moverlas.

## 📦 Requisitos

Este proyecto usa solo librerías estándar de Python. No requiere instalación adicional.

```bash
python main.py         # Para jugar en consola
python puzzle_gui.py   # Para jugar con interfaz gráfica
```
---

🧠 Lógica del juego
El tablero se genera aleatoriamente sin repetir fichas.

Sólo es posible mover una ficha si está adyacente al espacio vacío.

La lógica usa coordenadas simuladas (x, y) para validar movimientos.

🛠️ Estructura del proyecto 
- main.py: Juego en consola
- puzzle_gui.py: Juego con interfaz gráfica
- puzzle.py: Lógica del tablero
- utils/display.py: Visualización en consola
- requirements.txt: Dependencias (vacío por ahora)

## 🚀 Próximas mejoras
Consulta la tabla de planificación incluida para ver las funcionalidades pendientes.

## 👤 Autor
Aurelio González Salinas | Data Scientist | Experiencia Consultoría moral

---

## 📊 Tabla editable de planificación (copiar a Notion, Excel o Google Sheets)

| 🧩 Funcionalidad            | Estado     | Prioridad | Descripción técnica breve | ¿Requiere librería externa? |
|-----------------------------|-------------|-----------|--------------------------|------------------------------|
| Interfaz gráfica (Tkinter)  | ✅ Hecho    | Alta      | Botones interactivos, movimiento por clic   | No |
| Validación de victoria      | 🔜 Pendiente| Alta      | Verificar si el tablero está ordenado | No |
| Registro de movimientos     | 🔜 Pendiente| Media     | Contador y lista de movimientos | No |
| Reinicio del juego          | 🔜 Pendiente| Media     | Botón para reiniciar con nueva distribución aleatoria | No |
| Versión web (Flask)         | 🧊 Opcional | Baja      | Interfaz web para jugar desde navegador | Sí (Flask) |
| Versión móvil (Kivy)        | 🧊 Opcional | Baja      | App para Android/iOS | Sí (Kivy) |

---