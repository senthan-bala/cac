import pygame

import variables as v1
import draw as dr

width = v1.width
height = v1.height
black = v1.black
white = v1.white
finish_wait_time = v1.finish_wait_time

window = v1.window

end_font = v1.end_font
well_done_font = v1.well_done_font


def finish_game(minutes, seconds, is_red_ded):
    window.fill(white)
    if is_red_ded == False:
        stopwatch_time = dr.turn_time_into_text(minutes, seconds)
        end_message = "Your final time was " + stopwatch_time
        final_time = end_font.render(end_message, True, black, white)
        textrect = final_time.get_rect()
        textrect.center = (width / 2, height / 2)
        window.blit(final_time, textrect)
        if minutes >= 1:
            well_done_text = well_done_font.render(
                "Well done!", False, black, white
            )
            well_done = well_done_text.get_rect()
            well_done.center = (width / 2, (height / 2) + 140)
            window.blit(well_done_text, well_done)
    elif is_red_ded == True:
        end_message = "Blue Wins!"
        final_time = end_font.render(end_message, True, black, white)
        textrect = final_time.get_rect()
        textrect.center = (width / 2, height / 2)
        window.blit(final_time, textrect)
    pygame.display.update()
    pygame.time.delay(finish_wait_time)
