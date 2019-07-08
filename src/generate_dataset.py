import time
import numpy as np
from utils import TerminalText as tt
import constants
from generate_games import generateGames
from generate_labels import generateLabels
from generate_features import generateFeatures

start_time = time.time() # To measure script running time

# Number of rows/columns in the game board
N = 3 # N can"t be less than one 
areGamesGenerated = bool(0) # Change it to True if games are already saved in the generated folder
areLabelsGenerated = bool(0) # // // // // // labels // // // // // // //
areFeaturesGenerated = bool(0) # // // // // // features // // // // // // //

games = []
labels = []
features = []
M = 0

if N < 1:
    N = 1

print("")
print(tt.GREEN + "Generating Dataset..." + tt.END)
print(tt.GREEN + "Board Size: " + tt.END + f"{N}x{N}")

print("")
if not areGamesGenerated:
    games = generateGames(N)
    np.save(constants.GAMES_DIR, games) # Save generated games
else:
    print(tt.GREEN + "Games already generated. Loading games..." + tt.END)
    games = np.load(constants.GAMES_DIR)

M = len(games)

print("")
if not areLabelsGenerated:
    labels = generateLabels(N, games)
    np.save(constants.LABELS_DIR, labels) # Save generated labels
else:
    print(tt.GREEN + "Labels already generated. Loading labels..." + tt.END)
    labels = np.load(constants.LABELS_DIR)

print("")
if not areFeaturesGenerated:
    features = generateFeatures(games, M, pow(N, 2))
    np.save(constants.FEATURES_DIR, features) # Save generated features
else:
    print(tt.GREEN + "Features already generated. Loading features..." + tt.END)
    features = np.load(constants.FEATURES_DIR)

total_time = time.time() - start_time

print("")
print(tt.GREEN + "Generated dataset with " + tt.END + f"{M}" + tt.GREEN + " games in" + tt.END
        + f" {'%.2f' % total_time} " + tt.GREEN + "seconds." + tt.END)
print("")