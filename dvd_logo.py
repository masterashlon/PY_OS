import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as p
import random as r


print("\tA new window is open")
p.init()

sys.tracebacklimit = 0
display = p.display 
draw = p.draw
clock = p.time.Clock()
def dvd_logo():
    width = 760
    heigth = 576
    screen = display.set_mode((width, heigth), p.RESIZABLE)
    display.set_caption("DVD VIDEO")
    #myfont = p.font.SysFont("monospace", 90)
    dvd_logo = p.image.load("images/logo_dvd_video.png")
    logo = p.image.load("images/min_logo_dvd_video.png")
    display.set_icon(logo)
    width_logo = 150
    heigth_logo = 150
    dvd_logo = p.transform.scale(dvd_logo, (width_logo, heigth_logo))
    x_logo = int(r.random()* (width-width_logo-50))
    y_logo = int(r.random()* (heigth-heigth_logo-50))
    x_direction = 4
    y_direction = 4
    
    while True:
        if p.event.poll().type == p.QUIT:
            display.quit()
            p.quit()
            break
        screen.fill((0, 0, 240))
        #display.set_caption("FPS: " + str(round(clock.get_fps(), 2)))
        #dvd_logo = myfont.render("DVD", 1, (0, 255, 200))
        screen.blit(dvd_logo, (x_logo, y_logo))
        #draw.rect(screen, (200, 0, 0), p.Rect(x_rect, y_logo, width_rect, heigth_rect))  # center position is (dimension_screen - dimension)/2
        x_logo += x_direction
        y_logo += y_direction
        
        if x_logo < 0:
            x_direction = -x_direction
        elif x_logo > width - width_logo - 3:
            x_direction = -x_direction
            
        if y_logo < -40:
            y_direction = -y_direction
        elif y_logo > heigth - heigth_logo + 40:
            y_direction = -y_direction
            
        display.update()
        clock.tick(24)
        
dvd_logo()