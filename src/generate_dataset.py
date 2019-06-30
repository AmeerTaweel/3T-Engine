import time
import numpy as np
from utils import TerminalText as tt
from generate_games import generateGames
from generate_labels import generateLabels

start_time = time.time() # To measure script running time

# Number of rows/columns in the game board
N = 3 # N can't be less than one 
areGamesGenerated = False # Change it to True if games are already saved in the generated folder
areLabelsGenerated = False # Change it to True if labels are already saved in the generated folder

games = []
labels = []
M = 0

print("")
print(tt.GREEN + "Generating Dataset..." + tt.END)
print(tt.GREEN + "Board Size: " + tt.END + f"{N}x{N}")

if not areGamesGenerated:
    games = generateGames(N)
    M = len(games)
    np.save('./src/generated/games.npy', games) # Save generated games
else:
    print(tt.GREEN + "Games already generated. Loading games..." + tt.END)
    games = np.load('./src/generated/games.npy')

if not areLabelsGenerated:
    labels = generateLabels(N, games)
    np.save('./src/generated/labels.npy', labels) # Save generated labels
else:
    print(tt.GREEN + "Labels already generated. Loading labels..." + tt.END)
    labels = np.load('./src/generated/labels.npy')

total_time = time.time() - start_time
running_time_in_seconds = "%.2f" % total_time # Formatted running time

print(tt.GREEN + "Generated dataset with " + tt.END + f"{M}" + tt.GREEN + " games in" + tt.END
        + f" {running_time_in_seconds} " + tt.GREEN + "seconds." + tt.END)
print("")