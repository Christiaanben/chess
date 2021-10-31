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
        for col in range(8):
            self.pieces.append(Pawn((col, 1), color=PieceColor.WHITE))
            self.pieces.append(Pawn((col, 6), color=PieceColor.BLACK))

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
