import tkinter as tk
import random


class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rompecabezas 3x3")
        self.board = self.generate_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.draw_board()

    def generate_board(self):
        numbers = list(range(1, 9)) + ['']
        random.shuffle(numbers)
        return [numbers[i:i+3] for i in range(0, 9, 3)]

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                btn = tk.Button(self.root, text=str(value), width=6, height=3,
                                command=lambda x=i, y=j: self.try_move(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return i, j

    def try_move(self, i, j):
        empty_i, empty_j = self.find_empty()
        if abs(empty_i - i) + abs(empty_j - j) == 1:
            self.board[empty_i][empty_j], self.board[i][j] = self.board[i][j], ''
            self.update_board()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = str(self.board[i][j])


if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGUI(root)
    root.mainloop()
