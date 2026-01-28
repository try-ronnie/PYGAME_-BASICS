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
# this creates a time memory(object) that stores time memory of running things outside the loops so its not reset everytime a frame is runned
# One golden rule to remember 🔑
# Pygame does NOT remember anything for you
# colour variables
WHITE = (255, 255, 255)
BLACK = (0 , 0,  0)
RED = (255 ,0 , 0)
GREEN = (0 , 255, 0)
BLUE = (0 , 0 , 255)


#importing the image and its starting point
girl = pygame.image.load('girl.png')
girl_x = 100
girl_y= 100
direction = 'right'

money = pygame.image.load('money.jpeg')
money_x = 600
money_y = 100



#creating game loop 
running  = True

while running:
        DISPLAYSURF.fill(WHITE)
        # since its just an animation of moving things without input 
        # we wont need to check for inputs
        # we'd rather just give boundaries for the direction
        # meaning that if its under  x = 280 just move the image 5 pixels
        if direction == 'right':
                girl_x += 5
                if girl_x == 650:
                        money_y = 600
                        direction = 'down'
        if direction == 'down':
                girl_y += 5
                if girl_y == 650 :
                        money_x = 10 
                        direction = 'left'
        if direction == 'left':
                girl_x -= 5
                if girl_x == 20:
                        money_y = 10
                        direction = 'up'
        if direction == 'up':
                girl_y -= 5
                if girl_y == 20:
                        money_x == 600
                        direction = 'right'
        DISPLAYSURF.blit(girl , (girl_x , girl_y))
        for event in pygame.get.event():
                if event == QUIT:
                        pygame.quit()
                        sys.exit() # closes the gui
        pygame.display.update()
        fps_timer.tick() ## checks and returns the milliseconds it took to run a single frame 
                        # if its too fast ... it slows it down to fit 30 frames of picture drawn in a single second
                        # it updates the outside memory since it checks the data of the time taken for that certain frame to occur




# Game loop (runs forever)
# This is where you:
# control time (FPS)
# handle input/events
# update game logic (movement, collisions, etc.)
# draw everything
# update the screen
# girl magnet
