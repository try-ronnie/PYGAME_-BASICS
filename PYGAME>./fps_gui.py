# Setup phase (runs once)
# This is where you:
# initialize pygame
# create the window (surface)
# load images
# define colors
# create the Clock
# define FPS
# set starting values

import pygame , sys
from pygame.locals import *

pygame.init( )# initialize the lib
DISPLAYSURF = pygame.display.set_mode((700 , 700)) # creating the surface and giving  tuple of dimensions
pygame.display.set_caption('CAT MOVING') # names the display surface

# fps settings
fps = 30 
fps_timer = pygame.time.Clock()# this returns  an object that manages fps with all the methods to tweak .... 
        # in short it adds fps functionalit to the program to give proper time based rendering of photos
fps_timer.tick(fps) # ches ks and returns the milliseconds it took to run a single frame 
                    # if its too fast ... it slows it down to fit 30 frames of picture drawn in a single second

# colour variables
WHITE = (255, 255, 255)
BLACK = (0 , 0,  0)
RED = (255 ,0 , 0)
GREEN = (0 , 255, 0)
BLUE = (0 , 0 , 255)




# Game loop (runs forever)
# This is where you:
# control time (FPS)
# handle input/events
# update game logic (movement, collisions, etc.)
# draw everything
# update the screen
# girl magnet
