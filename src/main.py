import numpy as np
import tensorflow as tf

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

# Split into training and test set
training_percentage = 0.7 # The remaining 1 - training_percentage will be the test percentage

# pylint: disable=unbalanced-tuple-unpacking
# The comment above prevents pylint from showing a false warning
Xy_training, Xy_test = np.split(Xy_shuffled, [int(training_percentage * M)])

# Separate examples and labels
X_training = Xy_training[:, : N]
y_training = Xy_training[:, N]

X_test = Xy_test[:, : N]
y_test = Xy_test[:, N]