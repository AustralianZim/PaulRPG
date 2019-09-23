import sys
import pygame
from pygame.locals import *

# Variables Init
tile_size = 16#px
grid_size = (16,18)#n x m tiles
## World tile matrix
world_map = [0 for x in range(grid_size[1])]*grid_size[0] # can probably use enums here
## Player position
position = [0, 0]

# Pygame Init
pygame.init()
## Initialise screen
screen = pygame.display.set_mode([x*tile_size for x in grid_size])
## Initialise player
player = pygame.Rect(position, (tile_size,tile_size))


# Game Loop
while 1:
## Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

### Handle arrow keys (could potentially be cleaned up)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position[0] -= 1
                player = player.move(-tile_size, 0)
            elif event.key == pygame.K_RIGHT:
                position[0] += 1
                player = player.move(tile_size, 0)
            if event.key == pygame.K_UP:
                position[1] -= 1
                player = player.move(0, -tile_size)
            elif event.key == pygame.K_DOWN:
                position[1] += 1
                player = player.move(0, tile_size)

## Draw screen            
    screen.fill((0,0,0)) # black background
    pygame.draw.rect(screen, (0,200,0), player)
    pygame.display.flip()
