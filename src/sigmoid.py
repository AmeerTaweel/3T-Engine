from math import exp

def sigmoid(z):
    return 1 / (1 + exp(-z))