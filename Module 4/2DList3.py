def draw_board(board, row, column, shape):
    board[row][column] = shape

    for r in board:
        for c in r:
            print(c, end="")
        print()
    
    print()

def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    draw_board(board, row, column, "X")
    
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    draw_board(board, row, column, "O")

    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    draw_board(board, row, column, "X")

    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    draw_board(board, row, column, "O")
    
if __name__ == "__main__":
    main()