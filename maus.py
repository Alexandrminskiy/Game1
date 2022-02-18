import pygame as pg
import sys

WHITE = (255,255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

sc = pg.display.set_mode((400,300))
sc.fill(WHITE)
pg.display.update()

# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#
#         if i.type == pg.KEYDOWN:
#             if i.key == pg.K_ESCAPE:
#                 sys.exit()
#
#         if i.type == pg.MOUSEBUTTONDOWN:
#             if i.button == 1:
#                 pg.draw.circle(sc, RED, i.pos, 20)
#                 pg.display.update()
#             elif i.button == 3:
#                 pg.draw.circle(
#                     sc, BLUE, i.pos, 20)
#                 pg.draw.rect(
#                     sc, GREEN,
#                     (i.pos[0] - 10,
#                      i.pos[1] - 10,
#                      20, 20))
#                 pg.display.update()
#             elif i.button == 2:
#                 sc.fill(WHITE)
#                 pg.display.update()
#     pg.time.delay(20)


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        pg.draw.circle(sc, BLUE, pos, 5)
        pg.display.update()
    pg.time.delay(20)
