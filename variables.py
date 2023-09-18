import pygame


# main variables
fps = 90
width = 900
height = 500
square_size = 20
square_speed = 2
obstacle_count = 25
obstacle_kills = False

finish_wait_time = 3000

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

window = pygame.display.set_mode((width, height))

pygame.font.init()

font = pygame.font.Font("freesansbold.ttf", 15)
end_font = pygame.font.Font("freesansbold.ttf", 70)
well_done_font = pygame.font.Font("freesansbold.ttf", 35)
menu_font = pygame.font.Font("freesansbold.ttf", 40)
