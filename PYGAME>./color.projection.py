# build the ground of the game
import pygame , sys
from pygame.locals import *

pygame.init() #
DISPLAYSURF = pygame.display.set_mode((500.500))
Name = pygame.display.set_caption()
# setting default display colours
#we also need to realise :
    #tuple for display for positional value is 2 (pygames cartesian plane)
    

running = True # true value
while running:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
        