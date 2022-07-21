import pygame
#initializing the pygame
pygame.init()
windows = pygame.display.set_mode((480,580))  #width,height
pygame.display.set_caption("@by pavan dharimireddy")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            print(event)
pygame.quit()
