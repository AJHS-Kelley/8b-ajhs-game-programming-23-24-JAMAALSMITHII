# Number Slider, by Jamaal Smith, based on a project by Al Sweigart, v0.0

import sys, random, pygame 
# sys module provides access to system resources (i.e. Operating System Commands)

from pygame.locals import*
# Allows us to call functions from pygame using just the fuction name instead of module.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for Game Board
BOARDWIDTH = 4 # COLUMNS
BOARDWIDTH = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # This is a maxium value! Won't make a slow computer run faster.
BLANK = None

# COLOR VALUES in (R, G, B) format.
# 0 = No Value, 255 = Max Value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQOUISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQOUISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # pixels

# BUTTON SETUP
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

# ESTABLISH WINDOW MARGINS
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)

# DIRECTIONS
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'