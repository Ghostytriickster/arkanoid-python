import pygame
from pygame.locals import *

# en attente de finnision

WHITE = (255,255,255)
GREEN = (0,255,0)
LACK = (0,0,0)
SIZE = (600, 400)
color = pygame.Color('lightskyblue3')
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)
lock = True

start_buttoon_hitbox = pygame.Rect(200, 75, 200, 50)

#create a surface object, image is drawn on it.
imp = pygame.image.load("U:\\Documents\\NSI_ex\\TerminalNSI\\startbutton.png").convert()
screen.blit(imp, (200, 75))
pygame.display.flip()

#pygame.draw.rect(screen,GREEN,start_buttoon_hitbox)

while lock :
    for event in pygame.event.get() :
        if event.type == QUIT :
            lock = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            x,y = mouse_pos
            #pygame.draw.rect(screen,GREEN,(x,y,100,40))
            
            if start_buttoon_hitbox.collidepoint(mouse_pos):
                pass
                pygame.draw.rect(screen, LACK, start_buttoon_hitbox)
                
            else:
                active = False
    pygame.display.update()
  
pygame.quit()
