import pygame , sys # imports the pygame module ... and system module (to terminate the program for now )
from pygame.locals import * # this imports all constants that exist eg QUIT , KEYDOWN, MOUSE POS etc
# pygame.locals holds the constants --- events that happen every time and dont change ---- heydown ---mouse positionig ----  quit ==== and many more

pygame.init() # allows the pygame library to run
DISPLAYSURF = pygame.display.set_mode((400,400)) # gives dimensions for surface creatin
pygame.display.set_caption('hello world') 
# rember that pygame .display works on the window surface

running = True
while running:# keeps the program alive .... meaning this code will always run untill running becomes false(through maybe a quit constant)
    for event in pygame.event.get(): # this gets all the events occuring on our window surface
        if event.type == QUIT: #if the event type is equal to the contant of QUIT event .... then run the quiting code            
            pygame.quit() # deactivates the pygame library
            sys.exit() # fully terminates the program
            #you can exchange the two but just to avoid bugs keep it that way
        else:
            pygame.display.update()# this updates the display according to the events 
            # but since this is just being able to get familiar with working around with a gui using pygame ..... 
            # i have no events yet linket to events handling that still run drawing function ... so i think i have a long way to go ...

    