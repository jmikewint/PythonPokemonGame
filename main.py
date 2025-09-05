from time import sleep

import pygame

pygame.init()
import requests
import time


width, height = 512, 384
BLACK = (128, 0, 0)

screen = pygame.display.set_mode((width, height))


image = pygame.image.load('ProfOak.jpg').convert_alpha()
image.set_alpha(0)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))

    for x in range(128):
        image.set_alpha(x)
        pygame.time.delay(1)



    pygame.display.update()

