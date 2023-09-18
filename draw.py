import pygame

import variables as v1

width = v1.width
height = v1.height
black = v1.black
window = v1.window


def draw_screen(red, blue, text, textrect, obstacles):
    window.fill((255, 255, 255))
    window.blit(text, textrect)
    pygame.draw.rect(window, (255, 0, 0), red)
    pygame.draw.rect(window, (0, 0, 255), blue)
    # obstacles
    [draw_rect(obstacle) for obstacle in obstacles]
    pygame.display.update()


def draw_rect(obstacle):
    pygame.draw.rect(window, black, obstacle)
