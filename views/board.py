import pygame
from pygame.sprite import Sprite


class BoardView(Sprite):
    FILE_NAME = './images/board_black_and_white.png'

    def __init__(self):
        super(BoardView, self).__init__()
        self.image = pygame.image.load(self.FILE_NAME)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


