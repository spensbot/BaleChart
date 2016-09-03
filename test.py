import pygame
from parameters import *
from functions import *

#Pygame initialization
pygame.init()
surface = pygame.display.set_mode((width,height))
font = pygame.font.SysFont("Courier", 16)

#initialize variables
cursor_pos = 5
switch = [0 for x in range(shift*blocks)]
switch[0] = 1
switch[4] = 2

fill = bunker_fill(switch)

draw_window(surface)
draw_materials(surface, fill, cursor_pos, font)
draw_schedule(surface, switch)
draw_cursor(surface, cursor_pos)

pygame.display.flip()

pygame.time.wait(1500)

pygame.quit()