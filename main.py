from generate_sudoku import get_sudoku
from solve_sudoku import draw, solve


if __name__ == '__main__':
    sugoku = get_sudoku()
    sudoku_board = sugoku['board']
    draw(sudoku_board)
    print('\n' + '*' * 22 + '\n')
    if solve(sudoku_board):
        draw(sudoku_board)
    else:
        print('I can not solve it!!!')
