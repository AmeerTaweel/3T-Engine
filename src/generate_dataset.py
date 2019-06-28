import numpy as np
import copy
from referee import getGameState
from utils import printS

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
    for i, prev_board in enumerate(prev_boards):
        if i % 100 == 0:
            printS(".")
        for i in range(size):
            current_board = copy.deepcopy(prev_board)
            if current_board[i] != 0: continue
            current_board[i] = p_type
            if getGameState(np.reshape(current_board, (-1, n))) == 0:
                # Prevent duplicates
                isUnique = True
                for board in current_boards:
                    if (board == current_board).all():
                        isUnique = False
                if isUnique:
                    current_boards.append(current_board)
    print("")
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
        printS(f"Generating games with {i + 1} moves")
        boards[i + 1] = playLevelDeeper(boards[i], N, (i % 2) + 1)
    return reduceDimensions(boards)

# This script will generate and save all possible valid uncompleted games.
# Games will be saved as 'dataset.npy' into the 'generated' folder.
N = 3 # N can't be less than one

print("Generating dataset")
print(f"Board size: {N}x{N}")

games = generateGames(N) # N = 3 is the default

print(f"Number of generated games: {len(games)}")

np.save('./src/generated/dataset.npy', games)