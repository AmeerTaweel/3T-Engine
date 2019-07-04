import numpy as np
import constants

def getWinner(isWinForX, isWinForO):
    if isWinForX:
        return constants.X_WINS
    elif isWinForO:
        return constants.O_WINS
    else:
        return constants.GAME_INCOMPLETE

def getGameState(board_state):
    """
    Return the state of a Tic Tac Toe game.

    Parameters
    ----------
    board_state (Numpy Array): Contains the current state of the board as:
        0: Empty cell
        1: X
        2: O

    Returns
    -------
    Integer: The state of the game. Possible results:
        0: Game incomplete
        1: X wins
        2: O wins
        3: Draw
    """
    N = len(board_state) # Get in for an N x N board
    WIN_FOR_X = np.full(N, constants.X, np.uint8)
    WIN_FOR_O = np.full(N, constants.O, np.uint8)

    # Check Rows
    for row in board_state:
        result = getWinner((row == WIN_FOR_X).all(), (row == WIN_FOR_O).all())
        if result > constants.GAME_INCOMPLETE:
            return result
    
    # Check Columns
    for i in range(N):
        column = board_state[:, i]
        result = getWinner((column == WIN_FOR_X).all(), (column == WIN_FOR_O).all())
        if result > constants.GAME_INCOMPLETE:
            return result
    
    # Check Diagonals
    diagonals = np.full((2, N), 0, np.uint8)
    for i in range(N): # Left Diagonal
        diagonals[0, i] = board_state[i, i]
    for i, j in enumerate(range(N - 1, -1, -1)): # Right Diagonal
        diagonals[1, i] = board_state[i, j]
    for diagonal in diagonals:
        result = getWinner((diagonal == WIN_FOR_X).all(), (diagonal == WIN_FOR_O).all())
        if result > constants.GAME_INCOMPLETE:
            return result
    if constants.EMPTY_CELL in board_state:
        return constants.GAME_INCOMPLETE
    return constants.DRAW