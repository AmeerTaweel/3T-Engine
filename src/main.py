import time
import numpy as np
import tensorflow as tf
from utils import TerminalText as tt

import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR) # Make TensorFlow log errors only

# Don't run this script before generating dataset

start_time = time.time() # To measure script running time

print("")
print(tt.GREEN + "Loading dataset..." + tt.END)

examples = np.load('./src/generated/features.npy')
labels = np.load('./src/generated/labels.npy')

M = examples.shape[0] # Number of examples
N = examples.shape[1] # Number of features

print(tt.GREEN + "Number of examples: " + tt.END + f"{M}")
print(tt.GREEN + "Number of features: " + tt.END + f"{N}")

# Merge examples and labels to shuffle
# We do this in order to keep each label in the same index of the corresponding example
Xy_shuffled = np.zeros((M, N + 1), np.uint8)
print(tt.GREEN + "Merging examples with labels in order to shuffle..." + tt.END)
for example, label, merge in zip(examples, labels, Xy_shuffled):
    merge[:N] = example
    merge[N] = label

print(tt.GREEN + "Shuffling dataset..." + tt.END)
np.random.shuffle(Xy_shuffled)

print(tt.GREEN + "Splitting dataset into training and test datasets..." + tt.END)

# Split into training and test set
training_percentage = 0.7 # The remaining 1 - training_percentage will be the test percentage

# pylint: disable=unbalanced-tuple-unpacking
# The comment above prevents pylint from showing a false warning
Xy_training, Xy_test = np.split(Xy_shuffled, [int(training_percentage * M)])

# Separate examples and labels
X_training = Xy_training[:, : N]
y_training = Xy_training[:, N]
m_training = len(X_training)

print(tt.GREEN + "Number of training examples: " + tt.END + f"{m_training}")

X_test = Xy_test[:, : N]
y_test = Xy_test[:, N]
m_test = len(X_test)

print(tt.GREEN + "Number of test examples: " + tt.END + f"{m_test}")