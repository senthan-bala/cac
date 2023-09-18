import pygame

import variables as v1

width = v1.width
height = v1.height
window = v1.window

black = v1.black
white = v1.white
red_color = v1.red
blue_color = v1.blue

def draw_screen(red, blue, text, textrect, obstacles):
    window.fill(white)
    window.blit(text, textrect)
    pygame.draw.rect(window, red_color, red)
    pygame.draw.rect(window, blue_color, blue)
    # obstacles
    [draw_rect(obstacle) for obstacle in obstacles]
    pygame.display.update()


def draw_rect(obstacle):
    pygame.draw.rect(window, black, obstacle)


def turn_time_into_text(mins, secs):
    min_amt = ("0" if mins < 10 else "") + str(mins)
    sec_amt = ("0" if secs < 10 else "") + str(secs)
    return min_amt + ":" + sec_amt
