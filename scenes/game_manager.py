import sys

import pygame
from pygame.event import Event
from pygame.locals import *

from views.board import BoardView
from views.piece import Pawn


class GameManager:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((512, 512))
        pygame.display.set_caption("AI Chess Game")

        self.board = BoardView()
        self.pawn = Pawn()

    def run(self):
        while True:
            for event in pygame.event.get():
                self._handle_exit(event)
            self.board.draw(self.display)
            self.pawn.draw(self.display)
            pygame.display.update()

    @staticmethod
    def _handle_exit(event: Event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
