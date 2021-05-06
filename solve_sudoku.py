def draw(sudoku):
    """
    get sudoku from input and draw
    :param sudoku:
    :return:
    """
    for row in range(9):
        if row % 3 == 0:
            print('-' * 25)
        for column in range(9):
            if column % 3 == 0:
                print('| ', end='')
            print(sudoku[row][column], end=' ')
        print('|', end='')
        print()
    print('-' * 25)


def find_free(sudoku):
    """
    get sudoku from input and check available free home in sudoku
    :param sudoku:
    :return:
    """
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                return row, column
    return False


def is_valid_guess(sudoku, guess, row, column):
    """
    get sudoku, guess(number) and row, column free home sudoku from input
    and check guess is valid in home sudoku
    :param sudoku:
    :param guess:
    :param row:
    :param column:
    :return:
    """
    for i in range(9):
        if (sudoku[row][i] == guess) or (sudoku[i][column] == guess):
            return False

    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if sudoku[r][c] == guess:
                return False
    return True


def solve(sudoku):
    """
    solve sudoku recursive
    :param sudoku:
    :return:
    """
    if not find_free(sudoku):
        return True

    row, column = find_free(sudoku)

    for guess in range(1, 9 + 1):
        if is_valid_guess(sudoku, guess, row, column):
            sudoku[row][column] = guess
            if solve(sudoku):
                return True
            sudoku[row][column] = 0
    return False
