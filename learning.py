import sys

import pygame

# starts pygame
pygame.init()

# default main surface: screen w/h
screen = pygame.display.set_mode((400, 500))

# clock obj used to keep a constant framerate
clock = pygame.time.Clock()

# test surface to overlay and play with: w/h
test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))

# so we create a rect based on the size of the test_surface object and then place it how we want.
# so we are going to ensure the rect is drawn  from center and with coords that are exactly 50% w/h of the default
# screen which would result in having the test_surface placed in the dead center of the screen.

# center puts the center of the rect at those coords
# topright puts the top right of the new rect at those coords
# and so forth. basically, the first param declares where the drawing starts at the 2nd param coords. and the
# size of the rect is whatever size the test_surface happens to be (100,200 in this case)
test_rect = test_surface.get_rect(center=(200, 250))

while True:
    # at the start of each loop, we are going check for every possible event.
    # here we are checking to see if the player is attempting to end the game.
    # if so, then pygame.quit() is run. this is basically the opposite of pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # if other things are still running, pygame.quit() may not suffice.
            sys.exit()
    # add some color to the default surface and overlay surface (RGB tuple)
    screen.fill((175, 210, 70))
    test_rect.right += 1
    # using the above established test_rect, we will use that to determine where the test_surface is drawn
    screen.blit(test_surface, test_rect)

    # draw all elements and then displays it on the main screen set above
    pygame.display.update()
    # ensures while loop will not execute > 60 times per second. 60 is the framerate.
    clock.tick(60)
