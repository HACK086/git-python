import numpy as np

np.random.seed(42)
np.random.RandomState(42)

print(np.random.random(42)(1))
print(np.random.random(42)(1))

import pygame, sys, time

pygame.init()
mx = 400
my = 400
playSurface = pygame.display.set_mode((mx, my))
pygame.display.set_caption("Тир")
image = pygame.image.load("tank.jpg").convert()
image = pygame.transform.scale(image, (77, 44))
image2 = pygame.image.load("cub.png").convert()
image2 = pygame.transform.scale(image2, (40, 30))
image3 = pygame.image.load("Sn.png").convert()
image3 = pygame.transform.scale(image3, (20, 20))
fpsController = pygame.time.Clock()
white = pygame.Color(255, 255, 255)

x = 228  # Для image
y = 33  # Для image
x2 = 250  # image2
y2 = 350  # image 2
line = [[0, 200]]  # Линия
red = pygame.Color(255, 0, 0)  # Цвета
lightslateblue = pygame.Color(0, 200, 255)  # Цвета
move_1 = False
move_2 = False
move_3 = False
move_4 = False
p = False
t1 = True
t2 = False
x3 = x  # Для image3
y3 = y  # Для image3
