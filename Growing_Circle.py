 
import pygame 

screen = pygame.display.set_mode((600,600)) 

#color
white = (255,255,255) 
blue = (0,0,255) 

screen.fill(white) 
pygame.display.update() 

#creating a class circle 
class Circle: 
    def __init__(self,color,pos,radius,width): 
        self.circle_surf = screen 
        self.circle_color = color
        self.circle_pos = pos 
        self.circle_radius = radius 
        self.circle_width = width

#creating objects 
circle = Circle(blue,(60,40),30,0)
