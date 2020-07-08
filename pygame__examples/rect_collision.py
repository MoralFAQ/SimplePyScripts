#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import random

import pygame


pygame.init()

color = (0, 0, 0)
sc = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
x, y = random.randrange(0, 500), random.randrange(0, 500)

fnt = pygame.font.Font(None, 40)

surf1 = pygame.Surface((100, 100))
surf1.fill((100, 100, 100))
rect1 = surf1.get_rect(topleft=(x, y))

surf2 = pygame.Surface((50, 50))
surf2.fill((255, 255, 255))
rect2 = surf2.get_rect()

while True:
    text = fnt.render("Collision!", True, color)

    sc.fill((0, 0, 0))
    sc.blit(surf1, rect1)
    sc.blit(surf2, rect2)
    sc.blit(text, (260, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            rect2 = surf2.get_rect(center=event.pos)
            break

    if rect2.colliderect(rect1):
        color = (200, 200, 200)
    else:
        color = (0, 0, 0)

    pygame.display.update()
    clock.tick(60)
