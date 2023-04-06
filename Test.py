import pygame
from pygame.locals import *
from random import *

pygame.init()
clock = pygame.time.Clock() # Horloge

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

size = (600, 400)
window = pygame.display.set_mode(size)
window.fill(white)


x = 250
y = 380
vel = 2
width = 100
height = 20
r=pygame.Rect(x, y, width, height)
pygame.draw.rect(window, black, r)
x_ball = 290
y_ball = 190
rayon = 20
pygame.draw.ellipse(window, red, (x_ball,y_ball, rayon, rayon))
vx = .2
vy = .1
def collision(fig_1, fig_2):
    if fig_2.right < fig_1.left:
        return False
    if fig_2.bottom < fig_1.top:
        return False
    if fig_2.left > fig_1.right:
        return False
    if fig_2.top > fig_1.bottom:
        return False
    return True
    

pygame.display.update()

lock = True


while lock: # boucle pour maintenir la fenêtre ouverte
    
    for event in pygame.event.get():
        if event.type == QUIT:
            lock = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<500:
        x += vel
    if y_ball <= 20:
        print("plafond")
        vy = -vy
        vx *= (0.75+0.5*random())
    if y_ball >= 380:
        vy = -vy
    if x_ball <= 0 or x_ball >= 580:
        vx = -vx
        
    y_ball = y_ball + vy
    x_ball = x_ball + vx
    window.fill(white)
    pygame.draw.rect(window, (black), (x, y, width, height))
    pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), 20, 20))
    pygame.display.update()
            


                
pygame.quit()
