import pygame 
pygame.init() 
screen = pygame.display.set_mode((600,600))  #width & height
screen.fill((255,255,255)) #To fill the sreen with white color 
pygame.display.update() 
running = True  

while True: 
    event = pygame.event.poll() 
    if event.type == pygame.MOUSEBUTTONDOWN:
        image = pygame.image.load("Game Dev 2/bulbonoff\Bulbon.jpg") #To load the image
        res_img = pygame.transform.scale(image,(200,200)) #To change images size
        screen.blit(res_img,(200,200)) #To place the image on a spacific position on the screen
        pygame.display.update() 

    
    elif event.type == pygame.MOUSEBUTTONUP:
        image = pygame.image.load("Game Dev 2/bulbonoff\Bulboff.jpg") 
        res_img = pygame.transform.scale(image,(200,200))
        screen.blit(res_img,(200,200))  
        pygame.display.update() 
   
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            running = False 
