import random
import sys, pygame
from pygame.math import Vector2
from settings import cell_number, cell_size


class FRUIT:

    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


class SNAKE:
    def __init__(self):
        # list containing all snake body parts as vectors
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            snake_body_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (255, 0, 0), snake_body_rect)

    def move_snake(self):
        body_double = self.body[:-1]
        body_double.insert(0, body_double[0] + self.direction)
        self.body = body_double[:]




pygame.init()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

Orange = FRUIT()
Snake = SNAKE()

SNAKE_IS_MOVING = pygame.USEREVENT
pygame.time.set_timer(SNAKE_IS_MOVING, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_IS_MOVING:
            Snake.move_snake()

    screen.fill((175, 215, 70))
    Orange.draw_fruit()
    Snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
