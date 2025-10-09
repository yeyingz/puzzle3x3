import random


class Puzzle3x3:
    def __init__(self):
        self.board = self.generate_board()

    def generate_board(self):
        numbers = list(range(1, 9)) + [' ']
        random.shuffle(numbers)
        return [numbers[i:i+3] for i in range(0, 9, 3)]

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return i, j

    def move(self, direction):
        x, y = self.find_empty()
        dx, dy = {'up': -1, 'down': 1, 'left': -
                  1, 'right': 1}.get(direction, (0, 0))
        new_x = x + (dx if direction in ['up', 'down'] else 0)
        new_y = y + (dy if direction in ['left', 'right'] else 0)

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
            return True
        return False
