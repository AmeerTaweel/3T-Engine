import numpy as np
import constants

def playRandomMove(game):
    empty_cells = []
    for i, cell in enumerate(game):
        if cell == constants.EMPTY_CELL:
            empty_cells.append(i)
    return np.random.choice(empty_cells)

