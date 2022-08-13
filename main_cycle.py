import pygame 
import math
import pyautogui
from ground import Ground
from character import Character
width, height= pyautogui.size()


pygame.init()
screen = pygame.display.set_mode([width, height])
FPS = 60
#clock = pygame.time.Clock()


# Importing and creating objects here
gameground = Ground(pygame)
char = Character(pygame)


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    screen.fill((0, 0, 0))
    pygame.display.flip()


pygame.quit()