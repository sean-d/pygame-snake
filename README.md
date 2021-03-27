# pygame-snake

This is an attempt at the classic game snake. 

## Logic of the game
We will be moving around in a grid more or less. This is due to the only allowing movement after so many pixels
and because of that, it will act like a grid.

Since the snake will move around in the above fashion, we can consider the areas that it moves through as blocks.

Blocks will either be open board, snake, or possibly collectible for points or for funsies. Probably points.

We will be keeping track of the snake as a list of different positions, or blocks.


## Collectibles 
Class-based. This will determine x/y position on the board, which will be random.