import numpy as np
import copy
from referee import getGameState

def reduceDimensions(matrix):
    """
    Decrease any list/matrix dimensions by one.

    Parameters
    ----------
    matrix: Multidimensional Array

    Returns
    -------
    list: The matrix after reducing it's dimensions.
    """
    # Doesn't accept vectors/(1-dimensional matrices)
    # If matrix is a vector return it without changes
    if (type(matrix[0]) is not list): return matrix
    new_matrix = []
    for item in matrix:
        new_matrix += item
    return new_matrix

def playLevelDeeper(prev_boards, n, p_type):
    size = pow(n, 2)
    current_boards = []
    for prev_board in prev_boards:
        for i in range(size):
            current_board = copy.deepcopy(prev_board)
            if current_board[i] != 0: continue
            current_board[i] = p_type
            if getGameState(np.reshape(current_board, (-1, n))) == 0:
                current_boards.append(current_board)
    return current_boards

def generateGames(N = 3):
    """
    Generates all possible valid uncompleted Tic Tac Toe games on an NxN board.

    Parameters
    ----------
    N (Int): Number of rows/columns in board

    Returns
    -------
    list: All possible valid uncompleted games.
    """
    if N < 1: # N can't be less than one
        N = 1
    NxN = pow(N, 2)

    base_board = [[np.full(NxN, 0, np.uint8)]]
    boards = base_board + ([[]] * (NxN)) # Generated boards will be put here

    for i in range(NxN - 1):
        boards[i + 1] = playLevelDeeper(boards[i], N, (i % 2) + 1)
    return reduceDimensions(boards[1 : len(boards)])

# This script will generate and save all possible valid uncompleted games.
# Games will be saved as 'dataset.npy' into the 'generated' folder.
N = 3 # N can't be less than one
games = generateGames(N) # N = 3 is the default
np.save('./src/generated/dataset.npy', games)