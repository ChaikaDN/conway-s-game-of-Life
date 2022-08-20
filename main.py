import random
import pygame
import events
from config import *


def draw_grid(screen, cell_size, screen_size):
    width, height = screen_size
    for posx in range(0, width, cell_size[0]):
        pygame.draw.line(screen, black, (posx, 0), (posx, height))
    for posy in range(0, height, cell_size[1]):
        pygame.draw.line(screen, black, (0, posy), (width, posy))


def print_text(screen, message, font_size, position):
    font = pygame.font.SysFont('Impact', font_size)
    text = font.render(message, True, black)
    back_rect = text.get_rect()
    position_center = [coord - rect_coord for coord, rect_coord in zip(position, back_rect.center)]
    back_rect.center = position
    pygame.draw.rect(screen, white, back_rect)
    screen.blit(text, position_center)


def count_neighbors(objects, position):
    count = 0
    neighbors = (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)
    for i, j in neighbors:
        try:
            i1 = position[0] + i
            j1 = position[1] + j
            if objects[i1][j1]:
                count += 1
        except IndexError:
            continue
    return count


def draw_cell(screen, cell_value, position, cell_size):
    if cell_value:
        pygame.draw.rect(screen, black, (position[0] * cell_size[0], position[1] * cell_size[1], *cell_size))


def refresh(cells):
    new_cells = [[x for x in row] for row in cells]
    for i in range(len(cells)):
        for j in range(len(cells)):
            if cells[i][j] and count_neighbors(cells, (i, j)) not in (2, 3):
                new_cells[i][j] = False
            elif not cells[i][j] and count_neighbors(cells, (i, j)) == 3:
                new_cells[i][j] = True
    return new_cells


def main():
    cell_size = [x // dimension for x in size]
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game of life')

    cells = [[random.choice((True, False)) for _ in range(dimension)] for _ in range(dimension)]

    while True:
        events.track()
        if events.is_running:
            screen.fill(white)
            if dimension < grid_rate:
                draw_grid(screen, cell_size, size)

            for i, row in enumerate(cells):
                for j, cell in enumerate(row):
                    draw_cell(screen, cell, (i, j), cell_size)

            cells = refresh(cells)
        else:
            print_text(screen, 'PAUSED', 50, screen.get_rect().center)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
