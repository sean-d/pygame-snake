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
        screen.blit(fruit, fruit_rect)

    def new_fruit(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10)]
        self.head = pygame.image.load('Images/head_right.png').convert_alpha()
        self.direction = Vector2(1, 0)
        self.score = 0

        self.head_up = pygame.image.load('Images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Images/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Images/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Images/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Images/body_bl.png').convert_alpha()

    def add_block_to_snake(self):
        if len(self.body) >= 2:
            last_item = self.body[-1]
        else:
            last_item = self.body[:]
        self.body.append(Vector2(last_item.x, last_item.y))

    def draw_head(self):
        if self.direction == (1, 0):
            self.head = self.head_right
        if self.direction == (-1, 0):
            self.head = self.head_left
        if self.direction == (0, -1):
            self.head = self.head_up
        if self.direction == (0, 1):
            self.head = self.head_down

    def draw_snake(self):
        self.draw_head()

        for i, block in enumerate(self.body):
            snake_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)

            if i == 0:
                screen.blit(self.head, snake_rect)

            elif not 0 <= i or not i == len(self.body) - 1:
                if self.body[i].x < self.body[i - 1].x or self.body[i].x > self.body[i - 1].x:
                    screen.blit(self.body_horizontal, snake_rect)
                if self.body[i].y < self.body[i - 1].y or self.body[i].y > self.body[i - 1].y:
                    screen.blit(self.body_vertical, snake_rect)
            else:
                if i == len(self.body) - 1:
                    if self.body[i].x < self.body[i - 1].x:
                        screen.blit(self.tail_left, snake_rect)
                    if self.body[i].x > self.body[i - 1].x:
                        screen.blit(self.tail_right, snake_rect)
                    if self.body[i].y < self.body[i - 1].y:
                        screen.blit(self.tail_up, snake_rect)
                    if self.body[i].y > self.body[i - 1].y:
                        screen.blit(self.tail_down, snake_rect)
                else:
                    pygame.draw.rect(screen, (255, 0, 0), snake_rect)

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
            print("your score: {}".format(Game.snake.score))
            self.snake.add_block_to_snake()
            self.fruit.new_fruit()

    def update(self):
        self.snake.move_snake()
        self.check_game_over()
        self.snake_eats_fruit()


pygame.init()
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
fruit = pygame.image.load('Images/apple.png').convert_alpha()

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
