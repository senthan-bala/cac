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
button_font = v1.button_font
go_font = v1.go_font
pygame.display.set_caption("Two Player Pacman")
gamemode_list=v1.gamemode_list

def menu_loop():
    not_chosen = True
    game_index=0
    clock = pygame.time.Clock()
    if game_index==0:
        button_choice = pygame.Rect(300, 200, 300, 100)
    elif game_index==1:
        button_choice = pygame.Rect(250, 200, 400, 100)
    go_button = pygame.Rect(400, 400, 100, 50)

    while not_chosen:
        clock.tick(fps)
        button_color=(42,42,206)
        go_button_color=(42,42,206)
        mouse_down=False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down=True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down=False
            if event.type == pygame.QUIT:
                not_chosen = False
                pygame.quit()
        mouse_x_pos = pygame.mouse.get_pos()[0]
        mouse_y_pos = pygame.mouse.get_pos()[1]
        if game_index==0:
            button_choice = pygame.Rect(300, 200, 300, 100)
        elif game_index==1:
            button_choice = pygame.Rect(250, 200, 400, 100)
        # print(mouse_x_pos, mouse_y_pos)
        # mouse_down=pygame.mouse.get_pressed()[0]
        button_color,mouse_on_button=check_if_mouse_on_button(mouse_x_pos,mouse_y_pos,button_choice,button_color)
        go_button_color,mouse_on_go_button=check_if_mouse_on_button(mouse_x_pos,mouse_y_pos,go_button,go_button_color)
        menu_button_clicked=check_if_clicked_button(mouse_down,mouse_on_button)
        go_button_clicked=check_if_clicked_button(mouse_down,mouse_on_go_button)
        if menu_button_clicked==True:
            game_index+=1
        if game_index==2:
            game_index=0
        go_text = go_font.render("GO", True, black, go_button_color)
        go_text_rect = go_text.get_rect()
        go_text_rect.center = (450,425)
        menu_text = button_font.render(gamemode_list[game_index], True, black, button_color)
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (450,250)
        window.fill(white)
        pygame.draw.rect(window, button_color, button_choice)
        pygame.draw.rect(window, go_button_color, go_button)
        window.blit(go_text,go_text_rect)
        window.blit(menu_text,menu_text_rect)
        pygame.display.update()
        if go_button_clicked==True:
            return game_index


def check_if_clicked_button(mouse_down,mouse_on_any_button):
    if mouse_down==True and mouse_on_any_button==True:
        clicked=True
        return clicked


def check_if_mouse_on_button(x,y,rect,button_color):
    if x>=rect.x and x<=(rect.x+rect.width) and y>=rect.y and y<=(rect.y+rect.height):
        button_color=(0,0,255)
        mouse_on_button=True
    else:
        button_color=(42,42,206)
        mouse_on_button=False
    return button_color, mouse_on_button


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
        current_time_rect = current_time.get_rect()
        current_time_rect.center = (50, 15)
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
        dr.draw_screen(red,blue,current_time,current_time_rect,obstacles,)
        frames += 1
        if players_collide == True:
            f1.finish_game(minutes, seconds, False)
            run = False



game_index = menu_loop()
if game_index==1:
    main_2_player_loop()
