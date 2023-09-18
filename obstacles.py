import pygame

from random import randint

import variables as v1


square_size = v1.square_size
width = v1.width
height = v1.height
obstacle_count = v1.obstacle_count


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
