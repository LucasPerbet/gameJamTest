import pygame
from constantes import *

class Raquette:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.image = pygame.image.load("img/raquette.png").convert_alpha()
        self.largeur = self.image.get_width()
        self.hauteur = self.image.get_height()
        self.pos = [20, (self.ecran.get_height() - self.hauteur) // 2]  # Centrer la raquette
        self.vitesse = VITESSE_RAQUETTE

    def render(self):
        self.ecran.blit(self.image, self.pos)

    def move(self, direction):
        if direction == HAUT and self.pos[1] > 0:
            self.pos[1] -= self.vitesse
        elif direction == BAS and self.pos[1] + self.hauteur < self.ecran.get_height():
            self.pos[1] += self.vitesse

    def collide_with_me(self, pos_objet: tuple, taille_objet: tuple):
        # Détection de collision avec la balle
        if self.pos[0] <= pos_objet[0] <= self.pos[0] + self.largeur and \
           self.pos[1] <= pos_objet[1] <= self.pos[1] + self.hauteur:
            return True
        elif self.pos[0] <= pos_objet[0] + taille_objet[0] <= self.pos[0] + self.largeur and \
             self.pos[1] <= pos_objet[1] + taille_objet[1] <= self.pos[1] + self.hauteur:
            return True
        return False
