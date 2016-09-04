import pygame
from parameters import *
from functions import *

#Pygame initialization
pygame.init()
surface = pygame.display.set_mode((width,height))
font = pygame.font.SysFont("Courier", 16)

#initialize variables
cursor_pos = 0
switch = [0 for x in range(step_count)]

# Loop Forever
while True:

    #read user input
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
    elif ev.type == pygame.KEYDOWN:
        key = ev.dict["key"]
        if key == 275:
            cursor_pos += 1
        elif key == 276:
            cursor_pos -= 1
        elif 49 <= key < 49+len(comp):
            switch[cursor_pos] = key-48
        cursor_pos = clamp(cursor_pos, 0, step_count -1)
    elif ev.type == pygame.MOUSEMOTION:
        print(ev)
        pos = ev.dict["pos"]
        x_pos = pos[0]
        if menu_width < x_pos < width:
            cursor_pos = int((x_pos-menu_width)/schedule_width*(shift*blocks + OT*blocks))

    #draw the window
    fill = bunker_fill(switch)
    draw_window(surface)
    draw_materials(surface, fill, cursor_pos, font)
    draw_schedule(surface, switch)
    draw_cursor(surface, cursor_pos)
    draw_header(surface)
    draw_ticks(surface, font)

    #render the window
    pygame.display.flip()

#when the game loop has ended
pygame.quit()

