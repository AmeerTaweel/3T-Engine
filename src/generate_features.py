import time
import numpy as np
from utils import TerminalText as tt
from utils import getPlayingType

def generateFeatures(games, M, b_size):
    start_time = time.time() # To measure script running time

    print(tt.BLUE + "Generating Features..." + tt.END)
    print("") # To prevent the code in the loop from erasing the "Board Size" line
    examples = np.zeros((M, b_size), np.uint8)
    
    for i, game in enumerate(games):
        percentage = "%.2f" % (((i + 1) / M) * 100) # Limit to two decimal points
        print(tt.ERASE + tt.BLUE + "Converting Games To Machine Learning Ready Features: " + tt.END + f"{percentage}%")
        p_type = getPlayingType(game)
        for j, cell in enumerate(game):
            if cell == p_type:
                examples[i][j] = 1
            elif cell != p_type and cell != 0:
                examples[i][j] = 2
    
    total_time = time.time() - start_time
    print(tt.BLUE + "Generated features for " + tt.END + f"{M}" + tt.BLUE + " games in"
        + tt.END + f" {'%.2f' % total_time} " + tt.BLUE + "seconds." + tt.END)
    
    return examples