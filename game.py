import random
import sys, pygame
from settings import cell_number, cell_size


class FRUIT:

    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def draw_fruit(self):
        # this will place the fruit in a grid-like position as everything is based on the size of each cell
        # position will be determined by the above vector2 x/y values
        # Rect expects ints. when working with Vector we get floats. So cast to int making things explicit.
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

Orange = FRUIT()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    Orange.draw_fruit()
    pygame.display.update()
    clock.tick(60)
