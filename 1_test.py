import pygame as pg
import sys
# здесь определяются константы,
# классы и функции
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
# здесь происходит инициация,
# создание объектов
pg.init()
pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
sc.fill(GREEN)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

    def update(self):
        if motion == LEFT:
            self.rect.x -= 5
        elif motion == RIGHT:
            self.rect.x += 5
        elif motion == UP:
            self.rect.y -= 5
        elif motion == DOWN:
            self.rect.y += 5


all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

x = 250
y = 300

pg.display.update()
motion = STOP
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
            elif i.key == pg.K_RIGHT:
                motion = RIGHT
            elif i.key == pg.K_UP:
                motion = UP
            elif i.key == pg.K_DOWN:
                motion = DOWN
        elif i.type == pg.KEYUP:
            if i.key in [pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN]:
                motion = STOP
    all_sprites.update()
    sc.fill(GREEN)
    all_sprites.draw(sc)
    # pg.draw.rect(sc, BROWN, (x,y,50,50))
    pg.display.update()
    # if motion == LEFT:
    #     x -= 5
    # elif motion == RIGHT:
    #     x += 5
    # elif motion == UP:
    #     y -= 5
    # elif motion == DOWN:
    #     y += 5
    clock.tick(FPS)
