# T3 Engine

**Triple Three Engine** is a Tic Tac Toe engine. It uses **Machine Learning (ML)** to predict the best move in a given Tic Tac Toe game. It can be trained to predict the best move in any board size, although the default is a **3 by 3** board.

## How to use

**Note: All scripts must be run from the root directory of the project in order to avoid any unwanted behavior.**

### Generate Dataset

To generate a set of all possible Tic Tac Toe positions in a certain board dimensions, with the best possible move for each position as labels, run the `generate_dataset.py` script in the `src/` folder. The default is a **3 by 3** board but you can change that by changing the variable `N`.
