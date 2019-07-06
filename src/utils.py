import collections
import constants

class TerminalText():
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ERASE = '\x1b[1A\x1b[2K'

def getPlayingType(game):
    cells_values = collections.Counter(game)
    X_OCCURRENCES = cells_values[1]
    O_OCCURRENCES = cells_values[2]
    if X_OCCURRENCES == O_OCCURRENCES:
        return constants.X
    return constants.O