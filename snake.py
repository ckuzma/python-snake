import os
from random import randrange
from termcolor import colored

# Define grid size
WIDTH = 16
HEIGHT = 8

# Define color, symbol
BG_TILE = colored('O', 'yellow')

# Define snake colors, symbols
SNAKE_1_TILE = colored('#', 'green')
SNAKE_2_TILE = colored('#', 'red')

class SnakeGrid:
    def __init__(self, width, height):
        self.grid = self.initGrid(width, height)
    
    def initGrid(self, init_width, init_height):
        # Create a one-dimensional list row
        grid_row = [BG_TILE * init_width]

        # Repeat the row and append to the grid
        grid = []
        x = 0
        while x < init_height:
            grid.append(grid_row)
            x+=1
        
        # Return it
        return grid

    def printGrid(self):
        """
        Lazy way of pretty-printing the grid out
        to the console.
        """
        y = 0
        while y < len(self.grid):
            row = self.grid[y]
            x = 0
            while x < len(row):
                print(row[x])
                x+=1
            y+=1

    def isValidAddress(self, x, y):
        """
        Checks if the square is taken already
        """
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return False
        if self.grid[y][x] != BG_TILE:
            return False
        return True
        

class SnakeGame:
    def __init__(self, width, height, snake_len=4):
        self.snake_grid = SnakeGrid(WIDTH, HEIGHT)
        self.snake_grid.printGrid()
        self.snakes = [self.initSnake(snake_len)]
    
    def initSnake(self, length):
        """
        Plots an initial snake
        """
        snake = []
        
        # Add points until length is matched
        r = 0
        while r < length:
            r+=1
            # Incomplete here! CONTINUE HERE!
            """
            from random import randrange
            print(randrange(10))
            """

        return snake



sg = SnakeGame(WIDTH, HEIGHT)
