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


x_barre, y_barre = 250, 380
vel = 0.3 # La vitesse de la barre
width, height = 100, 20
r=pygame.Rect(x_barre, y_barre, width, height)
pygame.draw.rect(window, black, r)
x_ball = 290
y_ball = 190
rayon = 20
pygame.draw.ellipse(window, red, (x_ball,y_ball, rayon, rayon))
vx = random() * 0.2 - 0.1
vy = .1
police = pygame.font.SysFont("monospace", 30)
game_over = False
cpt = 0
width_ball, height_ball = 20, 20
    

pygame.display.update()

lock = True

def not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window):
    window.fill(white)
    pygame.draw.rect(window, (black), (x_barre, y_barre, width, height))
    pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball))
    image_texte = police.render(str(cpt), 1, (0, 0, 0))
    window.blit(police.render(str(cpt), 1, (0, 0, 0)), (10, 10))
    pygame.display.update()
    return image_texte

def is_game_over(x_barre, y_barre, cpt, window):
    window.fill(white)
    police = pygame.font.SysFont("monospace", 50)
    image_texte = police.render ("GAME OVER", 1, (255, 0, 0))
    window.blit(image_texte, (170, 175))
    police = pygame.font.SysFont("monospace", 30)
    image_texte = police.render ("You touched your ball "+ str(cpt) + " time(s)" , 1, (255, 0, 0))
    window.blit(image_texte, (20, 225))
    x_barre = 2000
    y_barre = 2000
    pygame.display.update()
    return x_barre, y_barre, image_texte


while lock: # boucle pour maintenir la fenêtre ouverte
    
    for event in pygame.event.get():
        if event.type == QUIT:
            lock = False
        keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT] and x_barre>0:
        x_barre -= vel
        
    if keys[pygame.K_RIGHT] and x_barre<500:
        x_barre += vel
        
    if y_ball <= 20:
        vy = -vy * 1.05
        vx *= (0.75+0.5*random())
        
    if y_ball >= 380:
        vy = 0
        vx = 0
        vel = 0
        game_over = True
        
    if x_ball <= 0 or x_ball >= 580:
        vx = -vx * 1.05
        
    if y_ball >= 360 and x_ball > x_barre and x_ball < x_barre + 100:
        vy = -vy * 1.05
        vx *= (0.75+0.5*random())
        cpt += 1
        window.blit(image_texte, (10, 10))
        
    y_ball = y_ball + vy
    x_ball = x_ball + vx
    
    if not game_over:
        image_texte = not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window)
        
    if game_over:
        x_barre, y_barre, image_texte = is_game_over(x_barre, y_barre, cpt, window)
        

            

           
pygame.quit()
