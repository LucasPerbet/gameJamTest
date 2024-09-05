import pygame
from constantes import *
from random import randint

class Balle:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.vitesse = VITESSE_BALLE
        self.vect_dir = [-self.vitesse, self.vitesse]
        self.image = pygame.image.load("img/balle.png").convert_alpha()
        self.b_large = self.image.get_width()
        self.b_haut = self.image.get_height()
        self.pos = [(self.ecran.get_width() - self.b_large) // 2, (self.ecran.get_height() - self.b_haut) // 2]
    
    def move(self, raquette):
        tmp = [self.pos[0] + self.vect_dir[0], self.pos[1] + self.vect_dir[1]]
        collision = raquette.collide_with_me(tmp, (self.b_large, self.b_haut))
        
        if collision or tmp[0] <= 0 or tmp[0] + self.b_large >= self.ecran.get_width():
            self.vect_dir[0] = - self.vect_dir[0]  # Rebond horizontal
        
        if tmp[1] <= 0 or tmp[1] + self.b_haut >= self.ecran.get_height():
            self.vect_dir[1] = - self.vect_dir[1]  # Rebond vertical
        
        # Mise à jour de la position après le rebond
        self.pos[0] += self.vect_dir[0]
        self.pos[1] += self.vect_dir[1]
    
    def render(self):
        self.ecran.blit(self.image, self.pos)
