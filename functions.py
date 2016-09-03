from parameters import *

def bunker_fill(switch):
    fill = [list(initial_fill)]
    current = [0 for x in range(len(comp))]
    baled = 0
    last_baled = 0

    for x in range(0, step_count):
        for y in range(len(comp)):
            if x < blocks*shift:
                current[y] = fill[x][y] + comp[y]*TPH/blocks
            else:
                current[y] = fill[x][y]
        fill.append(list(current))

        if switch[x] > 0:
            baled = switch[x]
        if baled > 0:
            fill[x+1][baled-1] -= baler1[baled-1]/blocks
            if last_baled != baled:
                fill[x+1][baled-1] += baler1[baled-1]*change_over
        fill[x+1][baled-1] = clamp(fill[x+1][baled-1], 0, 10000)
        last_baled = baled

    return fill

def draw_window(surface):
    # draw the background
    surface.fill(background_color)
    # draw the menu background
    surface.fill(menu_color, (0, 0, menu_width, height))
    # draw the OT background
    surface.fill(OT_color, (menu_width + shift_width, 0, OT_width, height))

def draw_cursor(surface, cursor_pos):
    from_left = menu_width + cursor_pos*cursor_step
    surface.fill(cursor_color1, (from_left - cursor_width1/2, 0, cursor_width1, height))
    surface.fill(cursor_color2, (from_left - cursor_width2/2, 0, cursor_width2, height))

def draw_materials(surface, fill, cursor_pos, font):
    for row in range(len(comp)):
        from_top = row * row_height + row*row_padding*2 + row_padding
        fill_percent = fill[cursor_pos][row]/bunker[row]
        surface.fill((0,150,0),(0,from_top,fill_percent*menu_width,row_height))
        label = repr(row + 1) + ": " + material[row]
        label_text = font.render(label, True, label_color)
        surface.blit(label_text, (10, from_top + row_padding / 2))

def draw_schedule(surface, switch):
    baled = 0
    for i in range(len(switch)):
        if switch[i] > 0:
            baled = switch[i]
        if baled > 0:
            from_top = (baled -1) * row_height + (baled-1)* row_padding * 2 + row_padding
            from_left = menu_width + cursor_step * i
            surface.fill(schedule_color, (from_left, from_top, cursor_step+1, row_height))

def clamp(n, min, max):
    if n < min:
        n = min
    elif n > max:
        n = max
    return n
