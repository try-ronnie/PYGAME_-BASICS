# build the ground of the game
import pygame , sys
from pygame.locals import *

pygame.init() #
DISPLAYSURF = pygame.display.set_mode((500.500))
Name = pygame.display.set_caption()
# setting default display colours
#we also need to realise :
    #tuple for display for positional value is 2 (pygames cartesian plane)
    # inorder to give an object size 
    # we need to give the starting coordinates ..... then give the width and length of the object i pixels
    # 1 coordinate = 1 pixel 

    #eg . >code> pygame.Rect(10)


#ASSIGNING COLOURS VARIABLE 
# THIS IS TO MAKE VARIABLE ASSIGNING EASIER
BLACK = (0 , 0 , 0 )
WHITE = (255 ,255, 255)
RED  = (255 ,0 , 0)
GREEN = (0 ,255 , 0)
BLUE = (0, 0 ,255)
DISPLAYSURF.fill(WHITE)

#drawing the objects 
# pygame.draw.polygon (surface , colour , pointlist , width(thickness))
pygame.draw.line(DISPLAYSURF, BLACK ,(69,50) , (120,60) , 4)
pygame.draw.rect(DISPLAYSURF , RED , (180,210) ())



running = True # true value
while running:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
        