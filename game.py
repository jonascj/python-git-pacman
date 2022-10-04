# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Setup ##
pg.init()
screen = pg.display.set_mode((300,400))
pg.display.set_caption("Pac-Man (clone)")

x = 300/2 
y = 400/2 

running = True
while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x = x-5
            elif event.key == pg.K_RIGHT:
                x = x+5
            elif event.key == pg.K_UP:
                y = y-5
            elif event.key == pg.K_DOWN:
                y = y+5

    # Draw
    screen.fill((0,0,0))

    pg.draw.circle(screen, (220,220,0), (x, y), 20)
            

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    time.sleep(0.05)
