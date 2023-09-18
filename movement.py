import pygame

import variables as v1
import finish as f1
import obstacles as obs

width = v1.width
height = v1.height
square_size = v1.square_size
square_speed = v1.square_speed
obstacle_kills = v1.obstacle_kills

red_key_codes = {'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN, 'LEFT': pygame.K_LEFT, 'RIGHT': pygame.K_RIGHT}
blue_key_codes = {'UP': pygame.K_w, 'DOWN': pygame.K_s, 'LEFT': pygame.K_a, 'RIGHT': pygame.K_d}


def square_movements(red, blue, keys, obstacles, minutes, seconds):
    sqaure_movement(red, red_key_codes, keys, obstacles, minutes, seconds)
    sqaure_movement(blue, blue_key_codes, keys, obstacles, minutes, seconds)


def sqaure_movement(obj, key_codes, keys, obstacles, minutes, seconds):
    if keys[key_codes['UP']] and obj.y - square_speed > 0:
        obj.y -= square_speed
        collide = obs.check_for_obj_collision(obj, obstacles)
        if collide == True and obstacle_kills == False:
            obj.y += square_speed
        elif collide == True and obstacle_kills == True:
            f1.finish_game(minutes, seconds, True)
    if keys[key_codes['DOWN']] and obj.y + square_speed + square_size < height:
        obj.y += square_speed
        collide = obs.check_for_obj_collision(obj, obstacles)
        if collide == True and obstacle_kills == False:
            obj.y -= square_speed
        elif collide == True and obstacle_kills == True:
            f1.finish_game(minutes, seconds, True)
    if keys[key_codes['LEFT']] and obj.x - square_speed > 0:
        obj.x -= square_speed
        collide = obs.check_for_obj_collision(obj, obstacles)
        if collide == True and obstacle_kills == False:
            obj.x += square_speed
        elif collide == True and obstacle_kills == True:
            f1.finish_game(minutes, seconds, True)
    if keys[key_codes['RIGHT']] and obj.x + square_speed + square_size < width:
        obj.x += square_speed
        collide = obs.check_for_obj_collision(obj, obstacles)
        if collide == True and obstacle_kills == False:
            obj.x -= square_speed
        elif collide == True and obstacle_kills == True:
            f1.finish_game(minutes, seconds, True)

