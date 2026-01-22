import pygame , sys # imports the main pygame module eg pygame.init() pygame.display
from pygame.locals import * #imports constant from pygames locals submodule
# pygame constants are named values that represent event types , keys and flags

pygame.init() # starts the pygame ... to allow use of its modules
DISPLAYSURF = pygame.display.set_mode((400,300)) # this returns the surface object for the window ... it has a tuple that provide the length and width window in pixels
# remember that we always need a tuple for the 2 to bud them into one
# The pygame.Surface object (we will just call them Surface objects for short) returned isstored in a variable named DISPLAYSURF.
pygame.display.set_caption('hellow world')
#this lets txt appear in the top of the window#im realizing that pygame.display returns something called a surface object that has methods like set_mode (that give the length and width of the window surface ) , set_caption(gives us the title name to our window)
while True: # provide a state of contuinity / main game loop / meaning it never exist
    for event in pygame.event.get():

# a game loop / main loop - loop that does three thing
# 1.handles events
# 2.updates the game state
# 3.draws the game state to the screen

# by game state we just mean all the set of values for allt eh variables in a game programgi