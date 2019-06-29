import numpy as np
import collections
import copy
from referee import getGameState

class Node():
    def __init__(self, game):
        self.game = game
        self.children = []
        self.index = None

def getPlayingType(game):
    cells_values = collections.Counter(game)
    X_OCCURRENCES = cells_values[1]
    O_OCCURRENCES = cells_values[2]
    if X_OCCURRENCES == O_OCCURRENCES:
        return 1
    return 2

def genrateChildren(node, size, p_type):
    boards = []
    for i in range(size):
        nextLevel = Node(copy.deepcopy(node.game))
        if nextLevel.game[i] != 0: continue
        nextLevel.game[i] = p_type
        nextLevel.index = i
        boards.append(nextLevel)
    return boards

def minMax(node, n, isMax, goal):
    state = getGameState(np.reshape(node.game, (-1, n)))
    if  state > 0:
        if state == goal:
            return 10
        elif state == 3:
            return 0
        else:
            return -10

    # Decide wether we play X or O.
    p_type = getPlayingType(node.game)
    node.children = genrateChildren(node, pow(n, 2), p_type)
    if isMax:
        return max([minMax(child, n, False, goal) for child in node.children])
    return min([minMax(child, n, True, goal) for child in node.children])

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