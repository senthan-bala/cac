import pygame
# import os

import obstacles as obs
import draw as dr
import variables as v1

pygame.display.set_caption("Two Player Pacman")

fps = v1.fps
width = v1.width
height = v1.height
square_size = v1.square_size
square_speed = v1.square_speed
obstacle_count = v1.obstacle_count
obstacle_kills = v1.obstacle_kills
black = v1.black

window = v1.window

font = v1.font
end_font = v1.end_font
well_done_font = v1.well_done_font
menu_font = v1.menu_font

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
        window.fill((255, 255, 255))
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
        stopwatch_time = turn_time_into_text(minutes, seconds)
        current_time = font.render(stopwatch_time, True, (0, 0, 0), (255, 255, 255))
        textrect = current_time.get_rect()
        textrect.center = (50, 15)
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if frames > 60:
            seconds += 1
            frames -= 60
        if seconds > 60:
            minutes += 1
            seconds -= 60
        keys_pressed = pygame.key.get_pressed()
        square_movements(red, blue, keys_pressed, obstacles, minutes, seconds)
        players_collide = check_for_square_collision(red, blue)
        dr.draw_screen(
            red,
            blue,
            current_time,
            textrect,
            obstacles,
        )
        frames += 1
        if players_collide == True:
            finish_game(minutes, seconds, False)
            run = False


def square_movements(red, blue, keys, obstacles, minutes, seconds):
    # for red
    if keys[pygame.K_UP] and red.y - square_speed > 0:
        red.y -= square_speed
        collide = check_for_obj_collision(red, obstacles)
        if collide == True and obstacle_kills == False:
            red.y += square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, True)
    if keys[pygame.K_DOWN] and red.y + square_speed + square_size < height:
        red.y += square_speed
        collide = check_for_obj_collision(red, obstacles)
        if collide == True and obstacle_kills == False:
            red.y -= square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, True)
    if keys[pygame.K_LEFT] and red.x - square_speed > 0:
        red.x -= square_speed
        collide = check_for_obj_collision(red, obstacles)
        if collide == True and obstacle_kills == False:
            red.x += square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, True)
    if keys[pygame.K_RIGHT] and red.x + square_speed + square_size < width:
        red.x += square_speed
        collide = check_for_obj_collision(red, obstacles)
        if collide == True and obstacle_kills == False:
            red.x -= square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, True)

    # for blue
    if keys[pygame.K_w] and blue.y - square_speed > 0:
        blue.y -= square_speed
        collide = check_for_obj_collision(blue, obstacles)
        if collide == True and obstacle_kills == False:
            blue.y += square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, False)
    if keys[pygame.K_s] and blue.y + square_speed + square_size < height:
        blue.y += square_speed
        collide = check_for_obj_collision(blue, obstacles)
        if collide == True and obstacle_kills == False:
            blue.y -= square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, False)
    if keys[pygame.K_a] and blue.x - square_speed > 0:
        blue.x -= square_speed
        collide = check_for_obj_collision(blue, obstacles)
        if collide == True and obstacle_kills == False:
            blue.x += square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, False)
    if keys[pygame.K_d] and blue.x + square_speed + square_size < width:
        blue.x += square_speed
        collide = check_for_obj_collision(blue, obstacles)
        if collide == True and obstacle_kills == False:
            blue.x -= square_speed
        elif collide == True and obstacle_kills == True:
            finish_game(minutes, seconds, False)


def turn_time_into_text(mins, secs):
    min_amt = str(mins)
    sec_amt = str(secs)
    if secs >= 10 and mins >= 10:
        tim = min_amt + ":" + sec_amt
    if secs < 10 and mins < 10:
        tim = "0" + min_amt + ":0" + sec_amt
    if secs >= 10 and mins < 10:
        tim = "0" + min_amt + ":" + sec_amt
    if secs < 10 and mins >= 10:
        tim = min_amt + ":0" + sec_amt
    return tim


def check_for_square_collision(obj1, obj2):
    collide = False
    if obj1.colliderect(obj2):
        collide = True
    return collide


def check_for_obj_collision(square, obj_list):
    collide = False
    for obj in obj_list:
        if square.colliderect(obj):
            collide = True
    return collide


def finish_game(minutes, seconds, is_red_ded):
    window.fill((255, 255, 255))
    if is_red_ded == False:
        stopwatch_time = turn_time_into_text(minutes, seconds)
        end_message = "Your final time was " + stopwatch_time
        final_time = end_font.render(end_message, True, (0, 0, 0), (255, 255, 255))
        textrect = final_time.get_rect()
        textrect.center = (width / 2, height / 2)
        window.blit(final_time, textrect)
        if minutes >= 1:
            well_done_text = well_done_font.render(
                "Well done!", False, (0, 0, 0), (255, 255, 255)
            )
            well_done = well_done_text.get_rect()
            well_done.center = (width / 2, (height / 2) + 140)
            window.blit(well_done_text, well_done)
    elif is_red_ded == True:
        end_message = "Blue Wins!"
        final_time = end_font.render(end_message, True, (0, 0, 0), (255, 255, 255))
        textrect = final_time.get_rect()
        textrect.center = (width / 2, height / 2)
        window.blit(final_time, textrect)
    pygame.display.update()
    pygame.time.delay(4500)



main_2_player_loop()
# menu_loop()
