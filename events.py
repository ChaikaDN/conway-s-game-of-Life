import pygame
import sys


def track():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
