# pygame-snake

This is an attempt at the classic game snake. 

## Logic of the game
We will be moving around in a grid more or less. This is due to the only allowing movement after so many pixels
and because of that, it will act like a grid.

Since the snake will move around in the above fashion, we can consider the areas that it moves through as blocks.

Blocks will either be open board, snake, or possibly collectible for points or for funsies. Probably points.

We will be keeping track of the snake as a list of different positions, or blocks.

## Drawing and Alignment on the board
When looking at the draw methods for the fruit and snake, the following design decision was landed on:

The fruit and snake will be placed in a grid-like position as everything is based on the size of each cell position. So you take x/y vector position and multiply
it by the size of each cell and you wind up in the corresponding placement on the board.  The rand is done with -1 on the offchance that something will randomly generate
off the edge of the board when drawing the rects for the fruit

Worth noting: pygame.Rect expects ints. when working with Vector we get floats. So cast to int making things explicit.

## Collectibles 
Class-based. This will determine x/y position on the board, which will be random.

### Snake
This will work like the fruit except that we will store and draw multiple vectors vs. a single vector.

#### Movement
Snake is moved via user input. If no input is provided, it will move based on the last provided input (a straight line). 
Basically we are going to take the stored list that contains every snake element location (vector2) sans the 
last element, create a copy of that list, and add to the 0th element of that new structure, a head that is placed at the location of
the 0th position of the original snake + the direction from the user input. 1,0 for instance. If the head is currently at 2,3, and we 
move to the right, the new head position will be 2,3 + 1,0...new head location will be at 3,3. 

we do not want the snake moving all the time, so we need a timer. let's set this to move every 150ms. So we will create a pygame USEREVENT
and a pygame timer. When the timer reaches the defined amount of time, the custom event will be triggered. We can then use the same 
pygame.event.get() approach in the main game loop to check if that event has be triggered. If he has, then we simply call the move_snake method.

