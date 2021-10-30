import sys

import pygame
from pygame.event import Event
from pygame.locals import *

from views.board import BoardView
from views.piece import Pawn, PieceColor


class GameManager:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((512, 512))
        pygame.display.set_caption("AI Chess Game")

        self.board = BoardView()
        self.pieces = []
        self.pieces.append(Pawn((2, 3)))
        self.pieces.append(Pawn((2, 4), color=PieceColor.BLACK))

    def run(self):
        while True:
            for event in pygame.event.get():
                self._handle_exit(event)
            self.board.draw(self.display)
            for piece in self.pieces:
                piece.draw(self.display)
            pygame.display.update()

    @staticmethod
    def _handle_exit(event: Event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
