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

direction = None
running = True
while running:


    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_ESCAPE:
                running = False

    # Move
    if direction == "left":
        x = x - 5
    elif direction == "right":
        x = x + 5
    elif direction == "up":
        y = y - 5
    elif direction == "down":
        y = y + 5


    # Draw
    screen.fill((0,0,0))

    pg.draw.circle(screen, (220,220,0), (x, y), 20)
            

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    time.sleep(0.05)
