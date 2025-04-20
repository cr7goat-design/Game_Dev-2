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

    def draw(self): 
        self.Draw_Circle = pygame.draw.circle(self.circle_surf,
                                              self.circle_color,
                                              self.circle_pos,
                                              self.circle_radius,
                                              self.circle_width)

    def grow(self,r): 
        self.circle_radius = self.circle_radius + r  
        self.Draw_Circle = pygame.draw.circle(self.circle_surf,
                                              self.circle_color,
                                              self.circle_pos,
                                              self.circle_radius,
                                              self.circle_width)

#creating objects 
circle = Circle(blue,(60,40),30,0) 
ci = Circle("red",(100,100),5,1) 
running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
    
        if event.type == pygame.MOUSEBUTTONDOWN: 
            screen.fill((255,255,255)) 
            circle.draw() 
            ci.draw()
            pygame.display.update() 

        elif event.type == pygame.MOUSEBUTTONUP: 
            screen.fill((255,255,255)) 
            circle.grow(15)
            ci.grow(5)  
            pygame.display.update() 
