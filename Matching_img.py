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
screen.blit(ludo,(150,200)) 
screen.blit(templerun,(150,300)) 
screen.blit(candy_crush,(150,400)) 

#Font specifications gvn 
font=pygame.font.sysFont("Times New Roman",36) 
text=font.render("Ludo",True,(0,0,255)) 
text1=font.render("candycrush",True,(0,255,0)) 
text2=font.render("Subway_surfer",True,(255,0,0)) 
text3=font.render("templerun",True,(0,255,150)) 

#positioning of texts 
screen.blit(text,(350,100)) 
screen.blit(text,(350,200))
screen.blit(text,(350,300))
screen.blit(text,(350,400)) 
pygame.display.update() 

running = true
while running: 
    event = pygame.event.poll() 
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos() 
        pygame.draw.circle(screen,(128,115,15),(pos), 20,0) 
        pygame.display.update() 


    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos() 
        pygame.draw.line(screen, (0,255,0), (pos), (pos2),5) 
        pygame.draw.circle(screen,(128,115,15),(pos), 20,0) 
        pygame.display.update() 

    #to quit the game 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
    
    pygame.display.update() 
 
