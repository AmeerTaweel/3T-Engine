import numpy as np
import tensorflow as tf
import constants

def playRandomMove(game):
    empty_cells = []
    for i, cell in enumerate(game):
        if cell == constants.EMPTY_CELL:
            empty_cells.append(i)
    return np.random.choice(empty_cells)

# Load trained model
model = tf.keras.models.load_model(constants.MODEL_DIR)

G = 10000 # Number of games against random player
N = constants.BOARD_SIZE

p_types = np.array([(1, 2), (2, 1)], np.uint8)

for i in range(G):
    current_game = np.full(N, constants.EMPTY_CELL, np.uint8)
    mp_type, rp_type = p_types[np.random.randint(0, 2)] # Model and random player playing types
    