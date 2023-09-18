import pygame

# import os
from random import randint

pygame.font.init()

# main variables
fps = 90
width = 900
height = 500
square_size = 20
square_speed = 2
obstacle_count = 25
obstacle_kills = False
black = (0, 0, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Two Player Pacman")

font = pygame.font.Font("freesansbold.ttf", 15)
end_font = pygame.font.Font("freesansbold.ttf", 70)
well_done_font = pygame.font.Font("freesansbold.ttf", 35)
menu_font = pygame.font.Font("freesansbold.ttf", 40)


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
        print('Megu msg - ', mouse_x_pos, mouse_y_pos)
        window.fill((255, 255, 255))
        not_chosen = False


def main_2_player_loop():
    obstacles = create_obstacles()
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
        draw_screen(
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


def create_obstacles():
    obs_position = (square_size, width, square_size, height)
    obs_dimension = (20, 125, 20, 125)
    return [create_obstacle(obs_position, obs_dimension) for i in range(obstacle_count)]


def create_obstacle(obs_position, obs_dimension):
    (x_min, x_max, y_min, y_max) = obs_position
    (w_min, w_max, h_min, h_max) = obs_dimension
    return pygame.Rect(
        randint(x_min, x_max),
        randint(y_min, y_max),
        randint(w_min, w_max),
        randint(h_min, h_max),
    )


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


# main_2_player_loop()
menu_loop()
