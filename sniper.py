import pygame, sys, time
from pygame.locals import *

pygame.init()

#Set up window
pygame.event.set_grab(0)
pygame.mouse.set_visible(1)
screen = pygame.display.set_mode((300,200))
shape = screen.convert_alpha()
pygame.display.set_caption("Sniper Alert")

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

#Draw on surface object
screen.fill(BLACK)

def alert():
    #Create a font
    font = pygame.font.Font(None,50)

    #Render the text
    text = font.render("Sniper Alert", True, RED)

    #Create a rectangle
    textRect = text.get_rect()

    #Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #Blit the text
    screen.blit(text, textRect)
    pygame.display.update()

    return press()

def press():
    t0 = time.clock()
    dt = 0

    while time.clock() - t0 < 1.5: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                dt = time.clock()- t0
                print dt
                return dt
            
alert()

#Exit
#pygame.quit()
#sys.exit()

#Run the game loop
"""while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()"""
