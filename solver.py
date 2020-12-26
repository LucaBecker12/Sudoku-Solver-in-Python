""" A sudoku solver """
from copy import deepcopy
import numpy as np


def solve(board):
    """
    A function used to solve a game of sudoku
    :param board: A 2D list, which represents a sudoku board
    :return: A 2D list of a solved sudoku game
    """
    temp = deepcopy(board)

    __help_solve__(temp)

    return temp


def __help_solve__(board):
    """
        A helper function which solves theh given board
        :param board: A sudoku board
        :return: True if solveable and False if not
        If True then the 2D sudoku grid is solved
    """
    find = __find_empty_square__(board)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):

        board[row][col] = i

        if is_valid(board):
            if __help_solve__(board):
                return True

        board[row][col] = 0

    return False


def __find_empty_square__(board):
    """
        A helper function which returns the next empty square on a sudoku board
        :param board: A 2D list, which represents a sudoku board
        :returns: tuple of row and col and None if there is no empty square
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board):
    """
        A function which validates a sudoku board
        :param board: A 2D list, which represents a sudoku board
        :return: True if valid and False if invalid
    """
    # Checking if all rows and columns are valid
    for i in range(len(board)):
        col = [row[i] for row in board]
        row = board[i]

        if not (__is_valid_line__(col) and __is_valid_line__(row)):
            return False

    # Checking if all 3x3 grids are valid

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            grid = []

            for i in range(row, row+3):
                for j in range(col, col+3):
                    grid.append(board[i][j])

            if not __is_valid_line__(grid):
                return False

    return True


def __is_valid_line__(temp):
    """
        A helper function which determines if a row or column or a 3x3 grid is valid or not
        :param line: A row or column of a sudoku board
        :return: True if valid and False if invalid
    """

    # Remove all zero's
    temp = list(filter(lambda x: x != 0, temp))

    # Check for invalid values
    if any(i < 0 or i > 9 for i in temp):
        return False

    # Checking for double values
    if is_valid_list(temp):
        return True
    else:
        return False


def is_valid_list(liste):
    """
        A function which determines wheter a list contains duplicates
        :param liste: A list which should be checked
        :return: True if valid and False if invalid
    """

    temp = set()
    for item in liste:
        if item in temp:
            return False
        else:
            temp.add(item)
    return True


def main():
    grid = [[1, 0, 3, 2, 0, 0, 0, 0, 0],
            [8, 6, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 4, 3, 6, 7],
            [0, 0, 0, 0, 2, 3, 8, 0, 6],
            [0, 0, 0, 1, 8, 0, 0, 4, 9],
            [0, 5, 0, 0, 0, 0, 0, 1, 3],
            [9, 0, 1, 7, 4, 0, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 6, 0, 0, 1, 0, 3, 0]]

    solved = solve(grid)
    count = 0
    for line, line2 in zip(grid, solved):
        if count != 4:
            print(f'{line}\t{line2}')
        else:
            print('{}{:^5}{}'.format(line, "->", line2))
        count += 1


if __name__ == "__main__":
    main()
