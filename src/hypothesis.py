import numpy as np
from sigmoid import sigmoid

def h(X, Theta):
    return np.vectorize(sigmoid)(X @ Theta)