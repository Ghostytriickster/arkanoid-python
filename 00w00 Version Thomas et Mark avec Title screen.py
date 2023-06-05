import pygame
from pygame.locals import *
from random import *
from math import *

pygame.init()
clock = pygame.time.Clock() # Horloge

save = open("save.txt","w")
save.write("0")
save.close()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

width_window, height_window = 960, 640

size = (width_window, height_window)
window = pygame.display.set_mode(size)
window.fill(white)

class objet_png_avec_une_hitbox():
    
    def __init__(self,image_name,coordonne):
        
        self.image_surface = pygame.image.load(image_name).convert() # objet du type surface avec l'image du png
        
        self.coordonne = (coordonne[0], coordonne[1]) #les coord x et y pour l'hitbox et l'image(l'objet surface)
        
        self.image_pos = window.blit(self.image_surface, (self.coordonne)) # position de l'image 
        
        self.hitbox = pygame.Rect( (self.coordonne), (self.image_surface.get_width(), self.image_surface.get_height())) # objet du type Rect
        #self.image_surface.get_rect() : à regarder 
        
        # pygame.display.flip() pour aficher l'image
        
    def is_cliked(self):
        mouse_pos = pygame.mouse.get_pos()
        x,y = mouse_pos
        if self.hitbox.collidepoint(mouse_pos):
            return True
        return False
    
def title_screen(current_score) :
        save = open("save.txt","r") # ouvre le fichier 
        saved_high_score = save.read() # lit le fichier
        
        window.fill(white) # Pour empecher que les sprites d'avant restent*
        font = pygame.font.Font(None, 34)
        text = font.render(saved_high_score, True, ('lightskyblue3'))
        textpos = text.get_rect(x = 336,y = 250)
        textpos_high_score = text.get_rect(x = 210,y = 250)
        start_button = objet_png_avec_une_hitbox("startbutton.png",(200,75)) # button
        
        if int(saved_high_score) < int(current_score) : # RECUPERER LE SCORE DE LA PARTIE 
            current_score = str(current_score) 
            save.write(current_score)
        save.close()
        
        text_high_score = font.render("high_score", True, (10,10,10))
        window.blit(text, textpos)
        window.blit(text_high_score, textpos_high_score)
        pygame.display.flip()

width, height = 160, 32 
x_barre, y_barre = (960/2) - (width/2), 640 - height
vel = 0.6 # La vitesse de la barre
r=pygame.Rect(x_barre, y_barre, width, height)
pygame.draw.rect(window, black, r)
x_ball = 464
y_ball = 288
rayon = 20
pygame.draw.ellipse(window, red, (x_ball,y_ball, rayon, rayon))
vx, vy = random() * 0.6 - 0.3, 0.8
police = pygame.font.SysFont("monospace", 30)
game_over = False
cpt = 0
width_ball, height_ball = 20, 20
play = False
cpt_acc = 0
cpt_game_over = 0
game_over = 0
cpt_game_over_ecran = 0
untouched_1 = True
untouched_2 = True



y_brick_1 = 100
brick_1 = pygame.Rect(0, 0, 960, y_brick_1)
y_brick_2 = 200
brick_2 = pygame.Rect(0, 0, 960, y_brick_2)

start = 0

start_button = objet_png_avec_une_hitbox("startbutton.png",(200,75)) # button

pygame.display.update()


    

def not_game_over(cpt, x_ball, y_ball, x_barre, y_barre, height, width, window): #Si le joue est toujours en cours
    window.fill(white) # Pour empecher que les sprites d'avant restent

    pygame.draw.rect(window, (black), (x_barre, y_barre, width, height)) # Redessine la barre avec ces nouvelles coordonnées
    pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball)) # Meme chose sur le cercle
    if untouched_1 :
        pygame.draw.rect(window, blue, brick_1)
    if untouched_2 :
        pygame.draw.rect(window, blue, brick_2)
    image_texte = police.render(str(cpt), 1, (0, 0, 0)) # Affiche un le nombre de rebond sur la barre
    window.blit(police.render(str(cpt), 1, (0, 0, 0)), (10, 10))
    pygame.display.update()
    return image_texte

# def is_game_over(x_barre, y_barre, cpt, window): # Si game over
#     window.fill(white)
#     police = pygame.font.SysFont("monospace", 80)
#     image_texte = police.render ("GAME OVER", 1, (255, 0, 0))
#     window.blit(image_texte, (272, 260))
#     police = pygame.font.SysFont("monospace", 48)
#     image_texte = police.render ("You touched your ball "+ str(cpt) + " time(s)" , 1, (255, 0, 0))
#     window.blit(image_texte, (32, 335))
#     x_barre = 2000
#     y_barre = 2000
#     pygame.display.update()
#     return x_barre, y_barre, image_texte

lock = True

while lock: # boucle pour maintenir la fenêtre ouverte
    
    if start == 0:
        title_screen(0)
        start = 1
    for event in pygame.event.get():
        if event.type == QUIT:
            lock = False # Si tu appuie sur la croix, cela ferme la fenetre
        keys = pygame.key.get_pressed()
        
    for event in pygame.event.get():
        if event.type == QUIT:
            lock = False # Si tu appuie sur la croix, cela ferme la fenetre
        keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT] and x_barre>0: # Si la touche fleche de gauche est appuyer, on retire la valeur vel (La vitesse de la barre) pour la faire aller à gauche. x_barre est la coordonnée x de la barre
        x_barre -= vel
        
    if keys[pygame.K_RIGHT] and x_barre<width_window -width: # Meme chose pour la fleche de droite
        x_barre += vel
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("right click")
        mouse_pos = pygame.mouse.get_pos()
        if start_button.is_cliked():
            window.fill(white) # Pour empecher que les sprites d'avant restent
            pygame.draw.rect(window, (black), (x_barre, y_barre, width, height)) # Redessine la barre avec ces nouvelles coordonnées
            pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball)) # Meme chose sur le cercle
            image_texte = police.render(str(cpt), 1, (0, 0, 0)) # Affiche un le nombre de rebond sur la barre
            window.blit(police.render(str(cpt), 1, (0, 0, 0)), (10, 10))
            for i in range (960):
                 pygame.draw.rect(window, (black), (i, 50, 136, 60))
                 i += 137
                
            pygame.display.update()
            play = True
            start = 1
        if game_over >= 1:
            vy, vx, vel = vy_game_over, vx_game_over, vel_game_over
      #if keys[pygame.K_SPACE] pour plus tard
    
    if play == True:
            
    
        if y_ball <= height_ball: # Si la balle touche le plafond
            C = (vx ** 2) + (vy ** 2)
            vy = -vy# la balle va s'inverser, elle change de sens.
            vx += random() * vx - vx / 2 # Pour plus de fun avec les rebonds
        
        if y_ball >= height_window - width_ball: # Si la balle touche le bas de l'écran sans toucher la barre
            vy_game_over, vy = vy, 0
            vx_game_over, vx = vx, 0 # Pour stopper la balle
            vel_game_over, vel = vel, 0 # Pour stopper la barre
            game_over = True # Pour lancer la fonction is_game_over
        
        
        if x_ball <= 0 or x_ball >= width_window - width_ball: # detecte les colisions sur la gauche ou droite de l'écran.
            vx = -vx
            
        
        if y_ball >= height_window - (width_ball + height)\
            and x_ball > (x_barre - width_ball + 3)\
            and x_ball < x_barre + width - 3:  #Pour detecter les si il y a une collision avec la barre, verifie si la balle est à la hauteur de la barre, et si elle est dans la barre(gauche = left, droite = left + width de la barre) Sussy baka.
            
            vy = - vy
            cpt += 1
            window.blit(image_texte, (10, 10))
        
        if height_window - (width_ball + height)<= y_ball:
            if abs(x_ball+width_ball-x_barre)<=4:
                vx *= -1
                
        if height_window - (width_ball + height)<= y_ball:
            if abs(x_ball-x_barre-width)<=4:
                vx *= -1
        
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
            window.fill(white) # Pour empecher que les sprites d'avant restent
            if y_ball <= y_brick_1:
                if untouched_1:
                    vy = -vy
                untouched_1 = False
            
            if y_ball <= y_brick_2:
                if untouched_2:
                    vy = -vy
                untouched_2 = False
        
            pygame.draw.rect(window, (black), (x_barre, y_barre, width, height)) # Redessine la barre avec ces nouvelles coordonnées
            pygame.draw.ellipse(window, red, (int(x_ball), int(y_ball), width_ball, height_ball)) # Meme chose sur le cercle
            image_texte = police.render(str(cpt), 1, (0, 0, 0)) # Affiche un le nombre de rebond sur la barre
            window.blit(police.render(str(cpt), 1, (0, 0, 0)), (10, 10))
            if untouched_1 :
                pygame.draw.rect(window, blue, brick_1)
            if untouched_2:
                pygame.draw.rect(window, blue, brick_2)
            pygame.display.update()
        
        if game_over:
            x_barre = 2000
            y_barre = 2000
            cpt_game_over = 1
            police = pygame.font.SysFont("monospace", 80)
            image_texte = police.render("GAME OVER", 1, (255, 0, 0))
            window.blit(image_texte, (272, 260))
            police = pygame.font.SysFont("monospace", 48)
            image_texte = police.render("Score "+ str(cpt) , 1, (255, 0, 0))
            window.blit(image_texte, (400, 335))
            image_texte = police.render("Highscore "+ str(cpt) , 1, (255, 0, 0))
            window.blit(image_texte, (400, 455))
            unouched_1, unouched_2 = True, True
            pygame.display.update()
            
                
            if keys[pygame.K_r]:
                game_over = False
                x_ball, y_ball = 464, 288
                x_barre, y_barre = (960/2) - (width/2), 640 - height
                vy, vx, vel = 0.8, random() * 0.6 - 0.3, 0.6
                cpt = 0
                pygame.display.update()
            
            print (untouched_1)

    
pygame.quit()

