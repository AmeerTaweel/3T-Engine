import time
import numpy as np
import tensorflow as tf
import constants
from generate_features import getFeatures
from referee import getGameState
from utils import TerminalText as tt

def playRandomMove(game):
    empty_cells = []
    for i, cell in enumerate(game):
        if cell == constants.EMPTY_CELL:
            empty_cells.append(i)
    return np.random.choice(empty_cells)

start_time = time.time() # To measure script running time

print(tt.YELLOW + "Testing Model Against Random Player..." + tt.END)

print(tt.YELLOW + "Loading trained model..." + tt.END)

# Load trained model
model = tf.keras.models.load_model(constants.MODEL_DIR)

G = 1000 # Number of games against random player
N = constants.BOARD_SIZE
NxN = pow(N, 2)

p_types = np.array([(1, 2), (2, 1)], np.uint8)

model_w, random_player_w, draws = 0, 0, 0

print(tt.YELLOW + "Games to play: " + tt.END + f"{G}")
print("") # To prevent the code in the loop from erasing the "Board Size" line

for i in range(G):
    percentage = "%.2f" % (((i + 1) / G) * 100) # Limit to two decimal points
    print(tt.ERASE + tt.YELLOW + "Games played against random player: " + tt.END + f"{percentage}%")
    current_game = np.full(NxN, constants.EMPTY_CELL, np.uint8)
    mp_type, rp_type = p_types[np.random.randint(0, 2)] # Model and random player playing types
    state = constants.GAME_INCOMPLETE
    for j in range(NxN):
        turn = (j % 2) + 1
        cell = None
        if turn == rp_type: # Random player turn
            cell = playRandomMove(current_game)
        else:
            features = getFeatures(current_game, NxN)
            prediction = model.predict(np.array([features]))
            cell = np.argmax(prediction)
        current_game[cell] = turn
        state = getGameState(np.reshape(current_game, (-1, N)))
        if state > 0:
            break
    if state == mp_type:
        model_w += 1
    elif state == rp_type:
        random_player_w += 1
    else:
        draws += 1

print(tt.YELLOW + "Model wins: " + tt.END + f"{model_w}" + tt.YELLOW + " out of "
    + tt.END + f"{G}" + tt.YELLOW + " games." + tt.END)
print(tt.YELLOW + "Random player wins: " + tt.END + f"{random_player_w}" + tt.YELLOW + " out of "
    + tt.END + f"{G}" + tt.YELLOW + " games." + tt.END)
print(tt.YELLOW + "Draw games: " + tt.END + f"{draws}" + tt.YELLOW + " out of "
    + tt.END + f"{G}" + tt.YELLOW + " games." + tt.END)
print(tt.YELLOW + "Model won " + tt.END + f"{'%.2f' % ((model_w / G) * 100)}%" + tt.YELLOW 
    + " of the games." + tt.END)
