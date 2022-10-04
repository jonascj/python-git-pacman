# Pac-Man clone made for learning/teaching
import time
import pygame as pg

pg.init()

screen = pg.display.set_mode((300,400))

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    screen.fill((0,0,0))

    pg.display.flip()

    time.sleep(0.05)

