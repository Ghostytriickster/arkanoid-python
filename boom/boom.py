# importing required library
import pygame
import time

pygame.init()
X = 600
Y = 600
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')

# trouve image et fait objet (woaw)


listeframe = []
for i in range(1, 36):
  listeframe.append(pygame.image.load("/home/ncr/boom/frame" + str(i)+str(".jpg")).convert())

def animator2000(framelist,coord1,coord2):
    for i in range(len(framelist)):
        scrn.blit(framelist[i], (coord1, coord2))
        pygame.display.update()
        time.sleep(0.01)

animator2000(listeframe, 0, 0)
pygame.display.flip()
status = True
while (status):

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            status = False

pygame.quit()
