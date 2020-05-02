# Reversi
Reversi game done with Test Driven Development

Minimax and alpha-beta pruning implemented.

Special feature:

<h2>Incremental depth search</h2>

In order for the AI to give an answer always in the given time interval, 
the AI algorithm is applied for each depth, starting with 1. If it still has time left, 
it calculates the next best move for the next depth (depth + 1),
it continues until it runs out of time. 

This is optimal because calculating the moves for the next depth grows exponentially. 
So to calculate the moves for the depth - 1, takes about 1-10%(depends on the branching factor) 
of calculating for the current depth



There is a TIMEOUT parameter that can be modified in GameEngine.py

<h2>The score function takes into account the difference between black and white pieces, 
as well as the difference between the nr of possible moves of each player</h2>

<h2>How to run</h2>

Comes with GUI.

1. First run ```pip install requirements.txt ```
2. Run the gui version by launching Drawing Engine
```
python DrawingEngine.py
```

To run the CLI version run
```
python GameEngine.py
```


<h2>Useful links</h2>
Mini-max and alpha-beta explained <a href="https://www.youtube.com/watch?v=l-hh51ncgDI&t=38s">Tutorial</a>

Game heuristics with explanation <a href="https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/">Click here</a>

