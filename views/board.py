import cocos
from cocos.sprite import Sprite
from pyglet import image


class BoardView(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        self._initialize_squares()
        label = cocos.text.Label(
            'Hello, world',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center',
            color=(50, 50, 50, 255)
        )
        label.position = 320, 240
        self.add(label)

        pawn = Sprite(image.load('./images/pawn_black.png'))
        pawn.position = 128, 64
        self.add(pawn)

    def _initialize_squares(self):
        self.squares = []
        for i in range(8):
            self.squares.append([])
            for j in range(8):
                image_file = './images/square.png' if (i + j) % 2 == 0 else './images/square_white.png'
                sprite = Sprite(image.load(image_file))
                sprite.position = i*64, j*64
                self.add(sprite)
                self.squares[-1].append(sprite)
