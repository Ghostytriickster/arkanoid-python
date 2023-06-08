"""Imports"""
import pygame
from pygame.locals import *
from random import *
from math import *

pygame.init()
clock = pygame.time.Clock()



"""Réglages fenêtre"""
x, y = 680, 680
window = pygame.display.set_mode((x, y))
pygame.display.set_caption('Sudoku')
fond = (255, 245, 230)
window.fill(fond)
#pygame.display.update()



"""Séléction difficultée"""
hard_mode = True
difficulty = 1



"""Polices d'écriture"""
font_size = 50
font = pygame.font.SysFont('Times New Roman', font_size)
font2 = pygame.font.SysFont('lightskyblue3', font_size)
font3 = pygame.font.SysFont('lightskyblue3', 70)



"""Génération valeurs"""
def generation_solution(valeurs_possibles):
    solution = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    
    for ligne in range(len(solution)):
        valeurs_disponibles = [_ for _ in valeurs_possibles]
        
        if ligne == 0:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 1:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val in solution[0][case]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 2:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val in solution[0][case] or val in solution[1][case]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 3:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 4:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne] or val in solution[3][case]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 5:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne] or val in solution[3][case] or val in solution[4][case]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
        
        if ligne == 6:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne] or val == solution[3][case][colonne] or val == solution[4][case][colonne] or val == solution[5][case][colonne]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
                    
        if ligne == 7:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne] or val == solution[3][case][colonne] or val == solution[4][case][colonne] or val == solution[5][case][colonne] or val == solution[6][case][colonne]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
                    
        if ligne == 8:
            for case in range(len(solution[ligne])):
                for colonne in range(len(solution[ligne][case])):
                    val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                    limite = 50
                    while val == solution[0][case][colonne] or val == solution[1][case][colonne] or val == solution[2][case][colonne] or val == solution[3][case][colonne] or val == solution[4][case][colonne] or val == solution[5][case][colonne] or val == solution[6][case][colonne] or val == solution[7][case][colonne]:
                        val = valeurs_disponibles[randint(0,len(valeurs_disponibles)-1)]
                        limite -= 1
                        if limite == 0:
                            return False
                    solution[ligne][case][colonne] = val
                    valeurs_disponibles.remove(val)
    return solution


def generation_sudoku(solution, difficultee):
    sudoku = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    for ligne in range(len(solution)):
        for case in range(len(solution[ligne])):
            for colonne in range(len(solution[ligne][case])):
                if randint(1,100) > difficultee:
                    sudoku[ligne][case][colonne] = solution[ligne][case][colonne]
    return sudoku


valeurs_possibles = [1,2,3,4,5,6,7,8,9]
solution = generation_solution(valeurs_possibles)
while solution == False:
    solution = generation_solution(valeurs_possibles)
#print('\n', solution[0], '\n', solution[1], '\n', solution[2], '\n\n', solution[3], '\n', solution[4], '\n', solution[5], '\n\n', solution[6], '\n', solution[7], '\n', solution[8], '\n')

sudoku = generation_sudoku(solution, difficulty)
hard_sudoku = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
for ligne in range(len(sudoku)):
    for case in range(len(sudoku[ligne])):
        for colonne in range(len(sudoku[ligne][case])):
            hard_sudoku[ligne][case][colonne] = sudoku[ligne][case][colonne]
#print('\n', sudoku[0], '\n', sudoku[1], '\n', sudoku[2], '\n\n', sudoku[3], '\n', sudoku[4], '\n', sudoku[5], '\n\n', sudoku[6], '\n', sudoku[7], '\n', sudoku[8], '\n')



"""Création grille pygame"""
d=15 #distance avec bord
l=y-(2*d) #longueur côté
c=l//9 #longeur case

fin=l+d #pos fin de ligne

def generation_grille(d, fin, c, couleur):
    for ligne_x in range(d,fin,c):
        pygame.draw.line(window, fond, (d, ligne_x), (fin, ligne_x), 12)
    for ligne_y in range(d,fin,c):
        pygame.draw.line(window, fond, (ligne_y, d), (ligne_y, fin), 12)
    
    num_ligne=0
    for ligne_x in range(d,fin,c):
        if num_ligne%3 != 0:
            pygame.draw.line(window, couleur, (d, ligne_x), (fin, ligne_x), 2)
        else:
            pygame.draw.line(window, couleur, (d-2, ligne_x), (fin, ligne_x), 5)
        num_ligne+=1

    num_ligne=0
    for ligne_y in range(d,fin,c):
        if num_ligne%3 != 0:
            pygame.draw.line(window, couleur, (ligne_y, d), (ligne_y, fin), 2)
        else:
            pygame.draw.line(window, couleur, (ligne_y, d), (ligne_y, fin), 5)
        num_ligne+=1

generation_grille(d, fin, c, (0,0,0))



"""Détermination positions chiffres"""
m=c//2 #milieu case

pos=[[(0,0) for _ in range(9)] for _ in range(9)]
for ligne in range(len(pos)):
    for colonne in range(len(pos[ligne])):
        pos[ligne][colonne] = (c*(ligne)+d+m-(font_size//4), c*(colonne)+d+m-(font_size//2))
#print(pos)



"""Affichage chiffres"""
for ligne in range(len(sudoku)):
    for case in range(len(sudoku[ligne])):
        for colonne in range(len(sudoku[ligne][case])):
            if sudoku[ligne][case][colonne] != 0:
                image_texte = font.render(str(sudoku[ligne][case][colonne]), 1, (0, 0, 0))
                window.blit(image_texte, pos[(case*3)+colonne][ligne])
pygame.display.update()
    #pygame.time.wait(100)



"""Bordures cases"""
bord = [[[(0,0),(0,0)] for _ in range(9)] for _ in range(9)]
for ligne in range(len(bord)):
    for colonne in range(len(bord[ligne])):
        bord[ligne][colonne][0] = (c*(colonne)+d, c*(ligne)+d)
        bord[ligne][colonne][1] = (c*(colonne)+d+c, c*(ligne)+d+c)
#print(bord)



"""Détecter quelle case cliquée"""
def detect_case(bord, mouse_pos, c):
    for ligne in range(len(bord)):
        for colonne in range(len(bord[ligne])):
            #print(bord[ligne][colonne], mouse_pos)
            if bord[ligne][colonne][0][0] <= mouse_pos[0] < bord[ligne][colonne][1][0] and bord[ligne][colonne][0][1] <= mouse_pos[1] < bord[ligne][colonne][1][1]:
                #pygame.draw.rect(window, (0,100,255), (bord[ligne][colonne][0], (c+2, c+2)), 7)
                return (colonne, ligne)
    return False

def draw_rect(bord, c, choix):
    pygame.draw.rect(window, (0,100,255), (bord[choix[1]][choix[0]][0], (c+2, c+2)), 7)
 


"""Vérifier si valeur entrée bonne"""
def verif(solution, choix, valeur):
    pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
    generation_grille(d, fin, c, (0,0,0))
    if hard_mode == False:
        if valeur == solution[choix[1]][choix[0]//3][choix[0]%3]:
            image_texte = font.render(str(valeur), 1, (0,140,0))
            window.blit(image_texte, pos[choix[0]][choix[1]])
            pygame.display.update()
            sudoku[choix[1]][choix[0]//3][choix[0]%3] = valeur
        else:
            image_texte = font.render(str(valeur), 1, (200,0,0))
            window.blit(image_texte, pos[choix[0]][choix[1]])
            pygame.display.update()
    else:
        image_texte = font.render(str(valeur), 1, (0,100,255))
        window.blit(image_texte, pos[choix[0]][choix[1]])
        pygame.display.update()
        if valeur == solution[choix[1]][choix[0]//3][choix[0]%3]:
            sudoku[choix[1]][choix[0]//3][choix[0]%3] = valeur
            



lock = True
game = True
choix = False
while lock: # boucle principale
    events_list = pygame.event.get()
    for event in events_list: # gestion des événements
        #print(pygame.mouse.get_pos())
        if event.type == QUIT: # fermeture de la fenêtre
            lock = False
        if event.type == KEYDOWN:
            if event.key == K_x:
                lock = False
        
        if game == True:
            if event.type == MOUSEBUTTONDOWN:
                generation_grille(d, fin, c, (0,0,0))
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                choix = detect_case(bord, mouse_pos, c)
                #print(choix)
                if hard_mode == False:
                    if choix != False:
                        if sudoku[choix[1]][choix[0]//3][choix[0]%3] == 0:
                            draw_rect(bord, c, choix)
                        else:
                            choix = False 
                else:
                    if choix != False:
                        if hard_sudoku[choix[1]][choix[0]//3][choix[0]%3] == 0:
                            draw_rect(bord, c, choix)
                        else:
                            choix = False
                pygame.display.update()
            
            if choix != False:
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        valeur = 1
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_2:
                        valeur = 2
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_3:
                        valeur = 3
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_4:
                        valeur = 4
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_5:
                        valeur = 5
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_6:
                        valeur = 6
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_7:
                        valeur = 7
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_8:
                        valeur = 8
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_9:
                        valeur = 9
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        verif(solution, choix, valeur)
                        choix = False
                    
                    if event.key == K_0:
                        pygame.draw.rect(window, fond, (bord[choix[1]][choix[0]][0], (c+2, c+2)))
                        generation_grille(d, fin, c, (0,0,0))
                        pygame.display.update()
                        choix = False
        
            if sudoku == solution:
                pygame.time.wait(2000)
                window.fill(fond)
                pygame.display.update()
                
                image_texte = font2.render("SUDOKU", 1, (0,100,255))
                window.blit(image_texte, (190,290))
                pygame.display.update()
                pygame.time.wait(1000)
                image_texte = font3.render("COMPLÉTÉ !", 1, (0,140,0))
                window.blit(image_texte, (190,320))
                
                pygame.display.update()
                game = False



pygame.quit()