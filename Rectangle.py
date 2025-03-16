import pygame 

screen = pygame.display.set_mode((600,600)) 

#colors
black = (0,0,0) 
white = (255,255,255) 
red = (255,0,0) 
green = (0,255,0) 
blue = (0,0, 255) 

screen.fill(white) 
pygame.display.update() 


# creating a class Regtangle 
class Rect: 
    def __init__(self,color,dimensions):
        self.rect_surf = screen 
        self.rect_color = color 
        self.rect_dimensions = dimensions 

    def draw(self): 
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, 
                                          self.rect_color,
                                          self.rect_dimensions) 
# creating instances/object
greenRect = Rect(green, (30,40,120,120)) 
blueRect = Rect(blue, (180,190,140,140)) 
orangeRect = Rect("orange", (340,350,180,180)) 

running = True 
while running:
    greenRect.draw() 
    blueRect.draw()
    orangeRect.draw()  
    pygame.display.update() 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
