import pygame
from pygame.locals import*
from time import*
screen = pygame.display.set_mode((600,600)) 
player_x = 200 
player_y = 200 

keys = [False,False,False,False] # for [up,left,down,right] 
player = pygame.image.load("Rocket.png") 
background = pygame.image.load("Space.png") 

while player_y < 600: 
    screen.blit(background, (0,0)) 
    screen.blit(player, (player_x,player_y)) 
    pygame.display.flip() 
