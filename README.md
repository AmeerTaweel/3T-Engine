# 3T Engine

**Triple Three Engine** is a Tic Tac Toe engine. It uses **Machine Learning (ML)** to predict the best move in a given Tic Tac Toe position. It can be trained to predict the best move in any board size, although the default is a **3 by 3** board. **Checkout [the project demo](https://ttt-engine.web.app/)**.

## How to use

**Note: All scripts must be run from the root directory of the project in order to avoid any unwanted behavior.**

### Generate Dataset

To generate a set of all possible Tic Tac Toe positions in a certain board dimensions, with the best possible move for each position as labels, run the `generate_dataset.py` script in the `src/` folder. The default is a **3 by 3** board but you can change that by changing the variable `BOARD_SIZE` in `src/constants.py`.

### Training The Model

To train a neural network on the dataset generated in the last step, run the `train_model.py` script. It will train a neural network using **TensorFlow**, and then save it to `src/generated/3t_model.h5` so it can be used later without the need to train it again each time you want to use it.

You can customize many aspects of the `train_model.py` by changing the following variables:

| Aspect                              | Variable Name | Type    | Default Value |
| ----------------------------------- |:-------------:|:-------:|:-------------:|
| Percentage of test set              | **t_p**       | `float` | 0.6           |
| Percentage of validation set __*__  | **v_p**       | `float` | 0.2           |
| Number of units in the hidden layer | **units**     | `int`   | 10**N** __*__ |
| Dropout probability                 | **d_prob**    | `float` | 0.05 __*__    |
| Number of epochs                    | **epochs**    | `int`   | 500           |

__*__ The remaining `1 - t_p - v_p` is the percentage of the test set.

__*__ **N** is the number of features.

__*__ You can turn dropout of by setting `d_prob` to **0**. Maximum is **1**.

**You should generate the dataset before running this script.**

### Testing The Model Against A Random Player

To test the trained model against a random player to check its performance, run the `test_against_random_player.py` script. You can specify for how many games you want to test by changing the variable `G`. When the test is done, you get the results for how many wins, losses, and draws occurred.
