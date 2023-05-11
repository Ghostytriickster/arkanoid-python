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

width_window, height_window = 960, 640

size = (width_window, height_window)
window = pygame.display.set_mode(size)
window.fill(white)

width, height = 160, 32 
x_barre, y_barre = (960/2) - (width/2), 640 - height
vel = 0.6 # La vitesse de la barre
r=pygame.Rect(x_barre, y_barre, width, height)
pygame.draw.rect(window, black, r)
x_ball = 464
y_ball = 288
rayon = 20
pygame.draw.ellipse(window, red, (x_ball,y_ball, rayon, rayon))
vx, vy = random() * 0.6 - 0.3, .3
police = pygame.font.SysFont("monospace", 30)
game_over = False
cpt = 0
width_ball, height_ball = 20, 20
play = False
cpt_acc = 0
    

pygame.display.update()


def not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window): #Si le joue est toujours en cours
    window.fill(white) # Pour empecher que les sprites d'avant restent

    pygame.draw.rect(window, (black), (x_barre, y_barre, width, height)) # Redessine la barre avec ces nouvelles coordonnées
    pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball)) # Meme chose sur le cercle
    image_texte = police.render(str(cpt), 1, (0, 0, 0)) # Affiche un le nombre de rebond sur la barre
    window.blit(police.render(str(cpt), 1, (0, 0, 0)), (10, 10))
    pygame.display.update()
    return image_texte

def is_game_over(x_barre, y_barre, cpt, window): # Si game over
    window.fill(white)
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
        
    if keys[pygame.K_LEFT] and x_barre>0: # Si la touche fleche de gauche est appuyer, on retire la valeur vel (La vitesse de la barre) pour la faire aller à gauche. x_barre est la coordonnée x de la barre
        x_barre -= vel
        
    if keys[pygame.K_RIGHT] and x_barre<width_window -width: # Meme chose pour la fleche de droite
        x_barre += vel
    if keys[pygame.K_SPACE]:
        play = True
    
    if play == True:
        game_over = False
        if y_ball <= height_ball: # Si la balle touche le plafond
            C = (vx ** 2) + (vy ** 2)
            vy = -vy# la balle va s'inverser, elle change de sens.
            vx += random() * vx - vx / 2 # Pour plus de fun avec les rebonds
        
        if y_ball >= height_window - width_ball: # Si la balle touche le bas de l'écran sans toucher la barre
            vy = 0
            vx = 0 # Pour stopper la balle
            vel = 0 # Pour stopper la barre
            game_over = True # Pour lancer la fonction is_game_over
        
        
        if x_ball <= 0 or x_ball >= width_window - width_ball: # detecte les colisions sur la gauche ou droite de l'écran.
            vx = -vx * 1.08
            
        
        if y_ball >= height_window - (width_ball + height) and x_ball > (x_barre - width_ball + 3) and x_ball < x_barre + width - 3:  #Pour detecter les si il y a une collision avec la barre, verifie si la balle est à la hauteur de la barre, et si elle est dans la barre(gauche = left, droite = left + width de la barre) Sussy baka.
            
            vy = - vy
            cpt += 1
            window.blit(image_texte, (10, 10))
        
        if cpt % 15 == 0 and cpt != 0 and acc == True and cpt_acc <= 3:
            vy *= 1.5
            acc = False
            cpt_acc += 1
            print("multiple de 5")
            
        elif cpt % 5 != 0:
            acc = True
        
        
        y_ball = y_ball + vy
        x_ball = x_ball + vx
    
        if not game_over:
            image_texte = not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window)
        
        if game_over:
            x_barre, y_barre, image_texte = is_game_over(x_barre, y_barre, cpt, window)
        if keys[pygame.K_r] and cpt != 0:
            print("Restart") 
            game_over == False
        
        

            

           
pygame.quit()
