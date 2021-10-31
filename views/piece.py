from enum import Enum
from typing import Tuple

import pygame
from pygame import Rect
from pygame.sprite import Sprite

from utils.logging import logger


class PieceColor(Enum):
    WHITE = 'white'
    BLACK = 'black'


class Piece(Sprite):
    FILE_NAME = 'unknown'

    def __init__(self, position: Tuple[int, int] = (0, 0), color: PieceColor = PieceColor.WHITE):
        super(Piece, self).__init__()
        self.x, self.y = position
        self.color = color

        filename = f'images/{self.FILE_NAME}_{self.color.value}.png'
        try:
            self.image = pygame.image.load(filename)
        except FileNotFoundError as error:
            logger.warning(f'Failed to initialize image for {self}. {error} for "{filename}"')
            self.image = pygame.image.load(f'images/{Piece.FILE_NAME}.png')

    @property
    def scaled_x(self):
        return self.x * self.image.get_width()

    @property
    def scaled_y(self):
        return self.y * self.image.get_height()

    @property
    def rect(self):
        return Rect(self.scaled_x, self.scaled_y, self.image.get_width(), self.image.get_height())

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Pawn(Piece):
    FILE_NAME = 'pawn'
