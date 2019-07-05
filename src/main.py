import numpy as np
# import tensorflow as tf

# Don't run this script before generating dataset

examples = np.load('./src/generated/features.npy')
labels = np.load('./src/generated/labels.npy')

M = examples.shape[0] # Number of examples
N = examples.shape[1] # Number of features

# Merge examples and labels to shuffle
# We do this in order to keep each label in the same index of the corresponding example
Xy_shuffled = np.zeros((M, N + 1), np.uint8)
for example, label, merge in zip(examples, labels, Xy_shuffled):
    merge[:N] = example
    merge[N] = label

np.random.shuffle(Xy_shuffled)

# Separate examples and labels
X = Xy_shuffled[:, : N]
y = Xy_shuffled[:, N]

Theta = np.zeros((N, 1), np.uint8)