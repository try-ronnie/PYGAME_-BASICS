import pygame , sys # imports the main pygame module eg pygame.init() pygame.display
from pygame.locals import * #imports constant from pygames locals submodule
# pygame constants are named values that represent event types , keys and flags

pygame.init() # starts the pygame ... to allow use of its modules
DISPLAYSURF = pygame.display.set_mode((400,300)) # this returns the surface object for the window ... it has a tuple that provide the length and width window in pixels
# remember that we always need a tuple for the 2 to bud them into one
# The pygame.Surface object (we will just call them Surface objects for short) returned isstored in a variable named DISPLAYSURF.
pygame.display.set_caption('hellow world')
#this is just like setting the surface of the game>>>>> window surface
#this lets txt appear in the top of the window#im realizing that pygame.display returns something called a surface object that has methods like set_mode (that give the length and width of the window surface ) , set_caption(gives us the title name to our window)
while True: # provide a state of contuinity / main game loop / meaning it never exist
    for one in pygame.event.get(): #checks for events multiples times in a sec and is gotten by pygame.event,get()
        #pygame.event.get() returns a list of all events that happened (like key presses, mouse clicks, window close). then (for event) it loops obver every list of event given in the list
        #one carries each event >>> this events are eventobjects like 
            # 1.event.type(what kind of event , KEYDOWN , QUIT )
            #  2.event.key (which key)
            # 3. event.pos (mouse positioning)
#so in short when a user does anything in the program window >>>> 
# a pygame.event.Event is created to record an event 
# Event object is created by the Pygame library to record this ―event‖. (This is a type of object called Event that exists in the event module, which itself is in the pygame module.
#we then use pygame.event.get() to get all of this object and return them into a list whic we then iterate over
# then we say if event.type == QUIT then do something ..... thats the full on logic

# a game loop / main loop - loop that does three thing
# 1.handles events
# 2.updates the game state
# 3.draws the game state to the screen

# by game state we just mean all the set of values for allt eh variables in a game programgi