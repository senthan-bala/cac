import pygame
# import os

import variables as v1
import draw as dr
import finish as f1
import movement as m1
import obstacles as obs


fps = v1.fps
width = v1.width
height = v1.height
square_size = v1.square_size
square_speed = v1.square_speed
obstacle_count = v1.obstacle_count
obstacle_kills = v1.obstacle_kills
black = v1.black
white = v1.white

window = v1.window

font = v1.font
end_font = v1.end_font
well_done_font = v1.well_done_font
menu_font = v1.menu_font

pygame.display.set_caption("Two Player Pacman, CAC project")

def menu_loop():
    not_chosen = True
    clock = pygame.time.Clock()
    two_player_button = pygame.Rect(300, 150, 300, 100)
    platformer_button = pygame.Rect(300, 350, 300, 100)

    while not_chosen:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_chosen = False
                pygame.quit()
        mouse_x_pos = pygame.mouse.get_pos()[0]
        mouse_y_pos = pygame.mouse.get_pos()[1]
        print(mouse_x_pos, mouse_y_pos)
        window.fill(white)
        pygame.draw.rect(window, (0, 0, 255), two_player_button)
        pygame.draw.rect(window, (0, 0, 255), platformer_button)
        pygame.display.update()


def main_2_player_loop():
    obstacles = obs.create_obstacles()
    frames = 0
    seconds = 0
    minutes = 0
    red = pygame.Rect(width - square_size, 0, square_size, square_size)
    blue = pygame.Rect(0, 0, square_size, square_size)
    clock = pygame.time.Clock()
    run = True
    while run:
        stopwatch_time = dr.turn_time_into_text(minutes, seconds)
        current_time = font.render(stopwatch_time, True, black, white)
        textrect = current_time.get_rect()
        textrect.center = (50, 15)
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if frames > fps:
            seconds += 1
            frames -= fps
        if seconds > 60:
            minutes += 1
            seconds -= 60
        keys_pressed = pygame.key.get_pressed()
        m1.square_movements(red, blue, keys_pressed, obstacles, minutes, seconds)
        players_collide = obs.check_for_square_collision(red, blue)
        dr.draw_screen(
            red,
            blue,
            current_time,
            textrect,
            obstacles,
        )
        frames += 1
        if players_collide == True:
            f1.finish_game(minutes, seconds, False)
            run = False


main_2_player_loop()
# menu_loop()
