# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg


## Load images ##
pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)

## Load images ##
ghost_images = []
for i in range(2):
    img = pg.image.load(f"images/ghost_{i}.png")
    img = pg.transform.scale(img, (32,32))
    ghost_images.append(img)

## Level ##
level = []
with open('level.txt', 'r') as level_file:
    for r, line in enumerate(level_file):
        row = []
        for c, char in enumerate(line):
            if char == "#":
                row.append("#")
            elif char == "p":
                pacman_row = r
                pacman_col = c
                direction = None
                row.append(" ")
            elif char == "g":
                ghost_row = r
                ghost_col = c
                row.append(" ")
            elif char == ".":
                row.append(".")
            else:
                row.append(" ")

        level.append(row)

num_rows = len(level)
num_cols = len(level[0])

## Screen setup ##
pg.init()
screen = pg.display.set_mode((num_cols*32, num_rows*32))
pg.display.set_caption("Pac-Man (clone)")

## Game Loop ##
direction = None
running = True
tick = 0
while running:


    # Event loop #
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

    # Move pacman #
    if direction == "left":
        if level[pacman_row][pacman_col-1] != "#":
            pacman_col -= 1
    elif direction == "right":
        if level[pacman_row][pacman_col+1] != "#":
            pacman_col += 1
    elif direction == "up":
        if level[pacman_row-1][pacman_col] != "#":
            pacman_row -= 1
    elif direction == "down":
        if level[pacman_row+1][pacman_col] != "#":
            pacman_row += 1

    # Move ghost #
    if random.choice([0,1]) == 0:
        dc = random.choice([-1,1])
        if level[ghost_row][ghost_col+dc] != "#":
            ghost_col += dc
    else:
        dr = random.choice([-1,1])
        if level[ghost_row+dr][ghost_col] != "#":
            ghost_row += dr 

    # Collision pacman/dots #
    if level[pacman_row][pacman_col] == ".":
        level[pacman_row][pacman_col] = " "

    # Draw level #
    screen.fill((0,0,0))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32

            if tile == "#":
                pg.draw.rect(screen, (20,20,220), pg.Rect(left+1, top+1, 32-2,32-2), 1)
            elif tile == ".":
                pg.draw.circle(screen, (255,220,150), (left+32/2, top+32/2), 3)

    # Draw pacman #
    r = int((tick/1)%6)
    if direction == "left":
        screen.blit(pacman_images[r], (pacman_col*32, pacman_row*32))
    elif direction == "right":
        screen.blit(pg.transform.rotate(pacman_images[r],180), (pacman_col*32, pacman_row*32))
    elif direction == "up":
        screen.blit(pg.transform.rotate(pacman_images[r],-90), (pacman_col*32, pacman_row*32))
    elif direction == "down":
        screen.blit(pg.transform.rotate(pacman_images[r],90), (pacman_col*32, pacman_row*32))
    else:
        screen.blit(pacman_images[0], (pacman_col*32, pacman_row*32))

    # Draw ghost #
    r = int((tick/1)%2)
    screen.blit(ghost_images[r], (ghost_col*32, ghost_row*32))
            

    # Update screen #
    pg.display.flip()

    # Framerate (limit by doing nothing) #
    tick += 1
    time.sleep(0.15)
