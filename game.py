import pygame
import random
import sys

from pygame.math import Vector2

from settings import cell_number, cell_size


class FRUIT:

    def __init__(self):
        self.x, self.y, self.pos = 0, 0, Vector2(0, 0)
        self.new_fruit()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def new_fruit(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.score = 0

    def add_block_to_snake(self):
        if len(self.body) >= 2:
            last_item = self.body[-1]
        else:
            last_item = self.body[:]
        self.body.append(Vector2(last_item.x, last_item.y + 1))

    def draw_snake(self):
        for block in self.body:
            snake_body_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (255, 0, 0), snake_body_rect)
            print(len(self.body))

    def move_snake(self):
        if len(self.body) >= 2:
            body_double = self.body[:-1]
        else:
            body_double = self.body[:]
        body_double.insert(0, body_double[0] + self.direction)
        self.body = body_double[:]


class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def check_game_over(self):
        # if x/y in head vector is less than  or equal 0 (far left wall) or greater than 20 (far right wall)
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_things(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def snake_eats_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.score += 1
            self.snake.add_block_to_snake()
            self.fruit.new_fruit()

    def update(self):
        self.snake.move_snake()
        self.check_game_over()
        self.snake_eats_fruit()


pygame.init()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
Game = GAME()

SNAKE_IS_MOVING = pygame.USEREVENT
pygame.time.set_timer(SNAKE_IS_MOVING, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_IS_MOVING:
            Game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if Game.snake.direction.y != 1:
                    Game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if Game.snake.direction.y != -1:
                    Game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if Game.snake.direction.x != 1:
                    Game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if Game.snake.direction.x != -1:
                    Game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    Game.draw_things()
    pygame.display.update()
    clock.tick(60)
