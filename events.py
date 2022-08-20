import pygame
import sys


is_running = True


def track():
    global is_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_running = not is_running
