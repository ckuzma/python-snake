import os
from termcolor import colored

# Define grid size
WIDTH = 16
HEIGHT = 8

# Define colors
SNAKE_1_COLOR = 'green'
SNAKE_1_SYMBOL = '#'
SNAKE_2_COLOR = 'red'
SNAKE_2_SYMBOL = '#'
BG_COLOR = 'yellow'

class SnakeGrid:
    def __init__(self, width, height):
        self.grid = self.initGrid(width, height)
    
    def initGrid(self, init_width, init_height):
        # Create a one-dimensional list row
        grid_row = [colored('O', BG_COLOR) * init_width]

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

    def changeGrid(self):
        pass

class Snake:
    def __init__(self, symbol, length):
        self.snake = self.initSnake(length)
    
    def initSnake(self, init_length):
        pass



sg = SnakeGrid(WIDTH, HEIGHT)
sg.printGrid()

print(colored('hello', 'red') + ' ' + colored('world', 'yellow'))