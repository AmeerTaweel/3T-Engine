import time
import numpy as np
from utils import TerminalText as tt

def generateFeatures(games, M, b_size):
    start_time = time.time() # To measure script running time

    print(tt.BLUE + "Generating Features..." + tt.END)
    print("") # To prevent the code in the loop from erasing the "Board Size" line
    features = np.zeros((M, b_size * 2), np.uint8)
    for i in range(2):
        for j in range(M):
            percentage = "%.2f" % (((j + 1) / M) * 100) # Limit to two decimal points
            print(tt.ERASE + tt.BLUE + "Converting Games To Machine Learning Ready Features: " + tt.END + f"{percentage}%")
            for o, k in enumerate(range(i, b_size * 2, 2)):
                features[j][k] = games[j][o] == i + 1

    total_time = time.time() - start_time
    running_time_in_seconds = "%.2f" % total_time # Formatted running time
    print(tt.BLUE + "Generated features for " + tt.END + f"{M}" + tt.BLUE + " games in"
        + tt.END + f" {running_time_in_seconds} " + tt.BLUE + "seconds." + tt.END)
    
    return features