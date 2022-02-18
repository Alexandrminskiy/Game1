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

pg.draw.rect(sc, BROWN, (250,300,50,50))

pg.display.update()

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
