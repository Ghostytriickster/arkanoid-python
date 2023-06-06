import pygame
from pygame.locals import *
from random import *
from math import *

pygame.init()
clock = pygame.time.Clock() # Horloge

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
magenta = (50, 0, 50)

width_window, height_window = 960, 640

size = (width_window, height_window)
window = pygame.display.set_mode(size)
window.fill(black)

width, height = 160, 32
x_barre, y_barre = (960/2) - (width/2), 640 - height
vel = 0.6 # La vitesse de la barre
r=pygame.Rect(x_barre, y_barre, width, height)
pygame.draw.rect(window, blue, r)
x_ball = 464
y_ball = 288
rayon = 20
pygame.draw.ellipse(window, red, (x_ball,y_ball, rayon, rayon))
vx, vy = random() * 0.6 - 0.3, .3
police = pygame.font.SysFont("monospace", 30)
game_over = False
cpt = 0
width_ball, height_ball = 32, 32

lst = []
lst_1 = []
c = 0
y_brick = 50
untouched = True


pygame.display.update()

for i in range(6):
    if len(lst) <= 5:
        lst.append(c) # stocke les coordonées x des briques
    c += 162

for i in range(len(lst)):
    brick = pygame.Rect(lst[i], 0, 160, y_brick)
    pygame.draw.rect(window, blue, brick)

def not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window, c): #Si le joue est toujours en cours
    window.fill(black) # Pour empecher que les sprites d'avant restent
    pygame.draw.rect(window, (blue), (x_barre, y_barre, width, height)) # Redessine la barre avec ces nouvelles coordonnées
    pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball)) # Meme chose sur le cercle
    if untouched :
        for i in range (len(lst)):
            for j in range(len(lst_1)):
                brick_1 = pygame.Rect(lst_1[j], 0, 160, y_brick)
                pygame.draw.rect(window, blue, brick_1)
            if x_ball >= lst[i-1] and x_ball <= lst[i] and y_ball <= y_brick:
                lst_1.append(lst[i-1])

    image_texte = police.render(str(cpt), 1, (255, 0, 0)) # Affiche un le nombre de rebond sur la barre
    window.blit(police.render(str(cpt), 1, (255, 0, 0)), (10, 10))
    pygame.display.update()
    return image_texte

def is_game_over(x_barre, y_barre, cpt, window): # Si game over
    window.fill(black)
    police = pygame.font.SysFont("monospace", 80)
    image_texte = police.render ("GAME OVER", 1, (255, 0, 0))
    window.blit(image_texte, (272, 260))
    police = pygame.font.SysFont("monospace", 48)
    image_texte = police.render ("You touched your ball "+ str(cpt) + " time(s)" , 1, (255, 0, 0))
    window.blit(image_texte, (32, 335))
    x_barre = 2000
    y_barre = 2000
    pygame.display.update()
    return x_barre, y_barre, image_texte

lock = True

while lock: # boucle pour maintenir la fenêtre ouverte
    
    for event in pygame.event.get():
        if event.type == QUIT:
            lock = False # Si tu appuie sur la croix, cela ferme la fenetre
        keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT] and x_barre>0: # Si la touche fleche de gauche est touchée, on retire la valeur vel
        x_barre -= vel # (La vitesse de la barre) pour la faire aller à gauche. x_barre est la coordonnée x de la barre
        
    if keys[pygame.K_RIGHT] and x_barre<width_window -width: # Meme chose pour la fleche de droite
        x_barre += vel
        
    if y_ball <= 0: # Si la balle touche le plafond
        vy = -vy * 1.05 # la balle va s'inverser, elle change de sens.
        vx *= (0.75+0.5*random()) # Pour plus de fun avec les rebonds
        
    if y_ball >= height_window - width_ball: # Si la balle touche le bas de l'écran sans toucher la barre
        vy = 0
        vx = 0 # Pour stopper la balle
        vel = 0 # Pour stopper la barre
        game_over = True # Pour lancer la fonction is_game_over  
        
    if x_ball <= 0 or x_ball >= width_window - width_ball: # Pour detecter les si il y a une collision avec la barre,
        vx = -vx * 1.05 # verifie si la balle est à la hauteur de la barre, et si elle est dans la barre(gauche = left, droite = left + width de la barre)
        
    if y_ball >= height_window - width_ball - height and x_ball > x_barre and x_ball < x_barre + width:  
        vx *= (0.75+0.5*random())
        vy = -vy
        cpt += 1
        window.blit(image_texte, (10, 10))
        
    y_ball = y_ball + vy
    x_ball = x_ball + vx
    
    if y_ball <= y_brick:
        vy = -vy
        cpt += 10
    
    if not game_over:
        image_texte = not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window, c)
        
    if game_over:
        x_barre, y_barre, image_texte = is_game_over(x_barre, y_barre, cpt, window)
           
pygame.quit()