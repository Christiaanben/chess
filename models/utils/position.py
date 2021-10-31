from dataclasses import dataclass
from enum import Enum, auto


class Column(Enum):
    a = auto()
    b = auto()
    c = auto()
    d = auto()
    e = auto()
    f = auto()
    g = auto()
    h = auto()


@dataclass
class Position:
    column: Column
    row: int

    def __post_init__(self):
        if not 1 <= self.row <= 8:
            raise Exception(f'Bad Position: {self.column.name}{self.row}')
