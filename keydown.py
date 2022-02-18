import sys
import pygame
from pygame import *
STOP = "stop"
RIGHT = "right"
LEFT = "left"
DOWN = "DOWN"
UP = "UP"
# Классы и функции
FPS = 60
W = 900
H = 300
WHITE = (255,255,255)
BLUE = (0,70,255)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# Координаты и радиус круга
x = W // 2
y = H // 2
r = 50
# Инцилизация,
# создание классов
pygame.init()
pygame.display.set_caption('Robinzon')

# Если надо до циклв отобразить
# какие-то объекты, обновляем экран
motion = STOP
# Главный цикл

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
                print(i.key, pygame.K_LEFT)
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
                print(i.key)
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
            elif i.key == pygame.K_ESCAPE:
                sys.exit()
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                motion = STOP
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    if motion == LEFT:
        x -= 5
    elif motion == RIGHT:
        x += 5
    elif motion == UP:
        y -= 5
    elif motion == DOWN:
        y += 5
    clock.tick(FPS)
