from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    black = 'black'
    white = 'white'


class Piece(ABC):

    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def valid_moves(self, board):
        """Return a list of valid moves given the position"""



