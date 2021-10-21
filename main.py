import cocos

from views.board import BoardView


def main():
    cocos.director.director.init()
    board_view = BoardView()
    main_scene = cocos.scene.Scene(board_view)
    cocos.director.director.run(main_scene)


if __name__ == '__main__':
    main()
