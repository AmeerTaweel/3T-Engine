import os
import time
import numpy as np
import tensorflow as tf
import tensorflowjs as tfjs
import matplotlib.pyplot as mplt
import constants
from utils import TerminalText as tt

# Don't run this script before generating dataset

def splitXy(Xy, n, c):
    X = Xy[:, 0 : n]
    y = Xy[:, n : n + c]
    m = len(Xy)
    return X, y, m

start_time = time.time() # To measure script running time

os.environ["TF_CPP_MIN_LOG_LEVEL"] = str(2)  # Make TensorFlow log errors only

print("")
print(tt.BLUE + "Loading dataset..." + tt.END)

examples = np.load(constants.FEATURES_DIR)
labels = np.load(constants.LABELS_DIR)

M = examples.shape[0] # Number of examples
N = examples.shape[1] # Number of features
C = labels.shape[1] # Number of classes

print(tt.BLUE + "Number of examples: " + tt.END + f"{M}")
print(tt.BLUE + "Number of features: " + tt.END + f"{N}")
print(tt.BLUE + "Number of classes: " + tt.END + f"{C}")

# Merge examples and labels to shuffle
# We do this in order to keep each label in the same index of the corresponding example
Xy_shuffled = np.zeros((M, N + C), np.uint8)
print(tt.BLUE + "Merging examples with labels in order to shuffle..." + tt.END)
for example, label, merge in zip(examples, labels, Xy_shuffled):
    merge[0 : N] = example
    merge[N : N + C] = label

print(tt.BLUE + "Shuffling dataset..." + tt.END)
np.random.shuffle(Xy_shuffled)

print(tt.BLUE + "Splitting dataset into training, validation and test sets..." + tt.END)

# Split into training and test set
t_p = 0.6 # Training set percentage
v_p = 0.2 # Validation set percentage. The remaining (1 - tp - vp) will be the test set percentage

# pylint: disable=unbalanced-tuple-unpacking
# The comment above prevents pylint from showing a false warning
Xy_train, Xy_val, Xy_test = np.split(Xy_shuffled, [int(t_p * M), int((t_p + v_p) * M)])

# Separate examples and labels
X_train, y_train, m_train = splitXy(Xy_train, N, C)
X_val, y_val, m_val = splitXy(Xy_val, N, C)
X_test, y_test, m_test = splitXy(Xy_test, N, C)

print(tt.BLUE + "Number of training examples: " + tt.END + f"{m_train}")
print(tt.BLUE + "Number of validation examples: " + tt.END + f"{m_val}")
print(tt.BLUE + "Number of test examples: " + tt.END + f"{m_test}")

units = 10 * N # Number of units in the hidden layer
d_prob = 0.05 # Dropout probability
epochs = 500

# Setup model layers
model = tf.keras.Sequential([
    tf.keras.layers.Dropout(d_prob),
    tf.keras.layers.Dense(units, tf.nn.relu),
    tf.keras.layers.Dense(C, tf.nn.softmax)
])

model.compile(tf.keras.optimizers.Adam(), "categorical_crossentropy", ["accuracy"])

print(tt.BLUE + "Training the model..." + tt.END)

# None is the batch size (We want to run through all examples in each epoch)
train_history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_val, y_val))

print(tt.BLUE + "Finished training the model." + tt.END)

mplt.xlabel("Number of Epochs") # Plot the loss over epochs
mplt.ylabel("Loss Magnitude")
mplt.plot(train_history.history["loss"])
mplt.plot(train_history.history["val_loss"])
mplt.show()

test_accuracy = model.evaluate(X_test, y_test)[1]
print(tt.BLUE + "Accuracy on test set: " + tt.END + f"{'%.2f' % (test_accuracy * 100)}%")

# Save entire model to an HDF5 file, so it can be used later without the need to be trained again
model.save(constants.MODEL_DIR)

print(tt.BLUE + "Model saved." + tt.END)

total_time = time.time() - start_time
print(tt.BLUE + "Trained and saved model in" + tt.END 
+ f" {'%.2f' % total_time} " + tt.BLUE + "seconds." + tt.END)