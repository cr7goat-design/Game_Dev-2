import pygame 
pygame.init() 
screen = pygame.display.set_mode((600,600)) 
screen.fill((255,255,255)) 
pygame.display.update() 

#loading images
subway_surfer = pygame.image.load("") 
ludo = pygame.image.load("") 
templerun = pygame.image.load("") 
candy_crush = pygame.image.load("") 

# position img on output screen 
screen.blit(subway_surfer,(150,100)) 
screen.blit(ludo,()) 
screen.blit(templerun,()) 
screen.blit(candy_crush,())
