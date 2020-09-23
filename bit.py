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
while True:

    playSurface.fill(white)
    playSurface.blit(image, [x, y])
    playSurface.blit(image2, [x2, y2])
    for element in line:
        pygame.draw.rect(playSurface, red, pygame.Rect(element[0], element[1], 900, 9))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # ========================= Тут вам надо написать код ========================
                x3 = x + 30
                y3 = y + 50

                p = True  # Проверка на истинность мишени

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                move_1 = True
            if event.key == pygame.K_RIGHT:
                move_2 = True

            if event.key == pygame.K_UP:
                move_3 = True

            if event.key == pygame.K_LEFT:
                move_4 = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN:
                move_1 = False
            if event.key == pygame.K_RIGHT:
                move_2 = False

            if event.key == pygame.K_UP:
                move_3 = False

            if event.key == pygame.K_LEFT:
                move_4 = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        # x, y = event.pos
    if move_1 == True:
        y += 4
        if y >= 170:
            y = 165

    if move_2 == True:
        x += 4
        if x >= 895:
            x = 895
    if move_3 == True:
        y -= 4
        if y < 5:
            y = 5
    if move_4 == True:
        x -= 4
        if x < 5:
            x = 5

    if p == True:
        # ========================= И тут наверное   ========================
        playSurface.blit(image3, [x3, y3])
        y3 += 10
        if y3 == x2 and y3 == y2 or y3 > 410:
            p = False
        y3 = y + 30