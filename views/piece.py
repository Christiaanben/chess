import pygame
from pygame.sprite import Sprite


class Piece(Sprite):
    FILE_NAME = None

    def __init__(self):
        super(Piece, self).__init__()
        self.image = pygame.image.load(self.FILE_NAME)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Pawn(Piece):
    FILE_NAME = 'images/pawn_black.png'
