import pygame
import random
import math

pygame.init()

l_fenetre = 1000
h_fenetre = 800

fenetre = pygame.display.set_mode((l_fenetre, h_fenetre))
pygame.display.set_caption('Systeme Solaire')

noir = (1,8,42)
blanc = (255,255,255)
jaune = (240, 210, 20)
blue = (0, 50, 220)
gris = (211, 211, 211)


def stars():
    liste = []
    for k in range(200):
        star = pygame.Rect(random.randint(0, l_fenetre), random.randint(0, h_fenetre), random.randint(1, 10), random.randint(1, 10))
        liste.append(star)
    return liste
new = stars()

def draw_stars(fenetre, couleur, lst):
    for i in lst:
        pygame.draw.circle(fenetre, couleur, (i[0], i[1]), random.randint(1, 3))
        
        
centre_x = l_fenetre // 2
centre_y = h_fenetre // 2

venus = pygame.Rect(l_fenetre // 2, h_fenetre // 1.5, 13, 13)
terre = pygame.Rect(l_fenetre // 3, h_fenetre // 3, 18, 18)
saturn = pygame.Rect(l_fenetre // 1.5, h_fenetre // 3, 27, 25)
jupiter = pygame.Rect(l_fenetre // 4, h_fenetre // 1.5, 35, 30)

    
def mouvement(angle, rayon, centre):
    x = centre[0] + rayon * math.cos(angle)
    y = centre[1] + rayon * math.sin(angle)
    return (int(x), int(y))

angle_v, royan_v = 0, 120
angle_s, royan_s = 0, 260
angle_t, royan_t = 0, 190

angle_j, royan_j = 0, 330

continuer = True
while continuer:
    fenetre.fill(noir)
    draw_stars(fenetre, blanc, new)
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                continuer = False 
    
    pygame.draw.circle(fenetre, jaune, (centre_x, centre_y), 55)
    pygame.draw.circle(fenetre, blanc, (centre_x, centre_y), royan_v, 1)
    pygame.draw.circle(fenetre, blanc, (centre_x, centre_y), royan_t, 1)
    pygame.draw.circle(fenetre, blanc, (centre_x, centre_y), royan_s, 1)
    pygame.draw.circle(fenetre, blanc, (centre_x, centre_y), royan_j, 1)
    
    
    pygame.draw.circle(fenetre, gris, mouvement(angle_v, royan_v, (centre_x, centre_y)), venus[2])
    angle_v += 0.02
    
    pygame.draw.circle(fenetre, blue, mouvement(angle_t, royan_t, (centre_x, centre_y)), terre[2])
    angle_t += 0.015
    
    pygame.draw.circle(fenetre, (255, 80, 55), mouvement(angle_j, royan_j, (centre_x, centre_y)), jupiter[2])
    angle_j += 0.005    
    
    pygame.draw.circle(fenetre, (255, 255, 153), mouvement(angle_s, royan_s, (centre_x, centre_y)), saturn[2])
    pygame.draw.circle(fenetre, (255, 255, 153), mouvement(angle_s, royan_s, (centre_x, centre_y)), saturn[2] + 18, 4)
    angle_s += 0.010
    
    
    pygame.time.delay(10)
    pygame.display.flip()
    
pygame.quit()