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
# finir le délire des classes et regarder la doc python 
class objet_png_avec_une_hitbox():
    
    def __init__(self,image_name,coordonne):
        
        self.image_surface = pygame.image.load(image_name).convert() # objet du type surface avec l'image du png
        
        self.coordonne = (coordonne[0], coordonne[1]) #les coord x et y pour l'hitbox et l'image(l'objet surface)
        
        self.image_pos = screen.blit(self.image_surface, (self.coordonne)) # position de l'image 
        
        self.hitbox = pygame.Rect( (self.coordonne), (self.image_surface.get_width(), self.image_surface.get_height())) # objet du type Rect
        #self.image_surface.get_rect() : à regarder 
        
        # pygame.display.flip() pour aficher l'image
        
    def is_cliked(self):
        mouse_pos = pygame.mouse.get_pos()
        x,y = mouse_pos
        if self.hitbox.collidepoint(mouse_pos):
            return True
        return False
# f = open("demofile.txt", "r")

# highscore = # lire le high scor sur le fichier 

start_button = objet_png_avec_une_hitbox("startbutton.png",(200,75))

pygame.font.init()
font = pygame.font.Font(None, 34)
text = font.render("high score", True, ('lightskyblue3'))
textpos = text.get_rect(x = 210,y = 250)
textpos_high_score = text.get_rect(x = 336,y = 250)

#if high_score < current_score :
    # f.open("filename.txt","w")
    # ecrire sur le fichier le nouveau high score 
    # current_score = high_score
    
text_high_score = font.render("high_score", True, (10,10,10))
    

screen.blit(text, textpos)
screen.blit(text_high_score, textpos_high_score)
#start_buttoon_hitbox = 

#create a surface object, image is drawn on it.
#imp = pygame.image.load("startbutton.png").convert()
#screen.blit(imp, (200, 75)) # position de l'image


pygame.display.flip()

#pygame.draw.rect(screen,GREEN,start_buttoon_hitbox)

while lock :
    for event in pygame.event.get() :
        if event.type == QUIT :
            lock = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            if start_button.is_cliked():
                
                # METTRE CODE DU JEU ICI
                
                
                
                
                
                pygame.draw.rect(screen, LACK, pygame.Rect(200, 75, 200, 50))
    pygame.display.update()
  
pygame.quit()
