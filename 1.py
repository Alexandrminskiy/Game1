import pygame as pg
import sys
import os

# Настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pg.image.load(os.path.join(img_folder, 'p1_jump.png'))

# здесь определяются константы,
FPS = 60
WIN_WIDTH = 600
WIN_HEIGHT = 700
GREEN = (140, 173, 0)
BROWN = (170, 100, 2)
STOP = "STOP"
RIGHT = "RIGHT"
LEFT = "LEFT"
DOWN = "DOWN"
UP = "UP"
motion = STOP
# здесь происходит инициация,
# создание объектов
pg.init()
pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# классы и функции
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

    def update(self):
        if motion == LEFT:
            self.rect.x -= 5
            # player.image = pg.transform.flip(player.image, 1, 0)

        elif motion == RIGHT:
            self.rect.x += 5

        elif motion == UP:
            self.rect.y -= 5
        elif motion == DOWN:
            self.rect.y += 5


all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
# pg.display.update()


while 1:
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_ESCAPE:
                sys.exit()
            elif i.key == pg.K_LEFT:
                motion = LEFT


                # player.image = pg.transform.rotate(player.image, 180)
            elif i.key == pg.K_RIGHT:
                motion = RIGHT

            elif i.key == pg.K_UP:
                motion = UP
            elif i.key == pg.K_DOWN:
                motion = DOWN

        elif i.type == pg.KEYUP:
            if i.key in [pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN]:
                motion = STOP
        if pg.key.get_pressed()[pg.K_LEFT]:
            player.image = pg.transform.flip(player.image, 1, 0)


    all_sprites.update()
    sc.fill(GREEN)
    all_sprites.draw(sc)
    pg.display.update()
    clock.tick(FPS)
