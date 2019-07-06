import numpy as np
import copy
from referee import getGameState
from utils import getPlayingType
import constants

class Node():
    def __init__(self, game):
        self.game = game
        self.children = []
        self.index = None

def genrateChildren(node, size, p_type):
    boards = []
    for i in range(size):
        nextLevel = Node(copy.deepcopy(node.game))
        if nextLevel.game[i] != constants.EMPTY_CELL: continue
        nextLevel.game[i] = p_type
        nextLevel.index = i
        boards.append(nextLevel)
    return boards

def minMax(node, n, isMax, goal):
    state = getGameState(np.reshape(node.game, (-1, n)))
    if  state > constants.GAME_INCOMPLETE:
        if state == goal:
            return constants.MM_WIN
        elif state == constants.DRAW:
            return constants.MM_DRAW
        else:
            return constants.MM_LOSS

    # Decide wether we play X or O.
    p_type = getPlayingType(node.game)
    node.children = genrateChildren(node, pow(n, 2), p_type)
    if isMax:
        return np.max([minMax(child, n, False, goal) for child in node.children])
    return np.min([minMax(child, n, True, goal) for child in node.children])

def predictBestNextMove(game, N):
    """
    Returns the best possible move in a given Tic Tac Toe position.

    Parameters
    ----------
    game: One-dimensional array, representing the board state.
    N (Int): Number of rows/columns in board

    Returns
    -------
    int: The index of the best move.
    """
    base = Node(game)
    goal = getPlayingType(base.game)
    nextMoves = genrateChildren(base, pow(N, 2), goal)

    bestScore = None
    nextBest = None

    for move in nextMoves:
        score = minMax(move, N, False, goal)
        if bestScore == None or score > bestScore:
            bestScore = score
            nextBest = move.index
    return nextBest