import pygame 
import math
import pyautogui
import os, os.path
from ground import Ground
from character import Character
width, height= pyautogui.size()


pygame.init()
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()


# Importing and creating objects here
gameground = Ground(pygame)
char = Character(pygame, './sprites/character1', (0,0), o_s=os)
#screen.set_alpha(char.image, 153)

running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    char.change_sprite()
    screen.fill((0, 0, 0))
    char.draw(screen)
    pygame.display.flip()


pygame.quit()