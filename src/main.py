import os
import time
import numpy as np
import tensorflow as tf
from utils import TerminalText as tt

os.environ["TF_CPP_MIN_LOG_LEVEL"] = str(2)  # Make TensorFlow log errors only

# Don't run this script before generating dataset

start_time = time.time() # To measure script running time

print("")
print(tt.GREEN + "Loading dataset..." + tt.END)

examples = np.load("./src/generated/features.npy")
labels = np.load("./src/generated/labels.npy")

M = examples.shape[0] # Number of examples
N = examples.shape[1] # Number of features
C = labels.shape[1] # Number of classes

print(tt.GREEN + "Number of examples: " + tt.END + f"{M}")
print(tt.GREEN + "Number of features: " + tt.END + f"{N}")
print(tt.GREEN + "Number of classes: " + tt.END + f"{C}")

# Merge examples and labels to shuffle
# We do this in order to keep each label in the same index of the corresponding example
Xy_shuffled = np.zeros((M, N + C), np.uint8)
print(tt.GREEN + "Merging examples with labels in order to shuffle..." + tt.END)
for example, label, merge in zip(examples, labels, Xy_shuffled):
    merge[0 : N] = example
    merge[N : N + C] = label

print(tt.GREEN + "Shuffling dataset..." + tt.END)
np.random.shuffle(Xy_shuffled)

print(tt.GREEN + "Splitting dataset into training and test datasets..." + tt.END)

# Split into training and test set
training_percentage = 0.7 # The remaining 1 - training_percentage will be the test percentage

# pylint: disable=unbalanced-tuple-unpacking
# The comment above prevents pylint from showing a false warning
Xy_training, Xy_test = np.split(Xy_shuffled, [int(training_percentage * M)])

# Separate examples and labels
X_training = Xy_training[:, 0 : N]
y_training = Xy_training[:, N : N + C]
m_training = len(X_training)

print(tt.GREEN + "Number of training examples: " + tt.END + f"{m_training}")

X_test = Xy_test[:, 0 : N]
y_test = Xy_test[:, N : N + C]
m_test = len(X_test)

print(tt.GREEN + "Number of test examples: " + tt.END + f"{m_test}")

# Setup model layers
model = tf.keras.Sequential([
    tf.keras.layers.Dense(N, tf.nn.sigmoid),
    tf.keras.layers.Dense(C, tf.nn.softmax)
])

model.compile(tf.keras.optimizers.Adam(), "categorical_crossentropy", ["accuracy"])

print(tt.GREEN + "Training the model..." + tt.END)

training_history = model.fit(X_training, y_training, epochs = 10)

print(tt.GREEN + "Finished training the model." + tt.END)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print('Accuracy on test dataset:', test_accuracy)