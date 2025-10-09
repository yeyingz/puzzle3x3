def display_board(board):
    print("\nRompecabezas 3x3:\n")
    for row in board:
        print(' | '.join(str(cell).rjust(2) for cell in row))
    print()
