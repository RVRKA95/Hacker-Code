import pygame
import random

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Python.io")
Clock = pygame.time.Clock()

# Snake Class
class Python:
    def __init__(self, x, y, width, height, speed, direction, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.color = color
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.snake_length = 1

    def change_direction(self, user_direct):
        if user_direct == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif user_direct == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif user_direct == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif user_direct == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"

    def move_snake(self):
        if self.direction == "UP":
            self.x_change = 0
            self.y_change = -self.speed
        elif self.direction == "DOWN":
            self.x_change = 0
            self.y_change = self.speed
        elif self.direction == "LEFT":
            self.y_change = 0
            self.x_change = -self.speed
        elif self.direction == "RIGHT":
            self.y_change = 0
            self.x_change = self.speed

        # Update position
        self.x += self.x_change
        self.y += self.y_change

    def check_borders(self):
        if self.x < 0:
            self.x = Width
        elif self.x > Width:
            self.x = 0
        elif self.y < 0:
            self.y = Height
        elif self.y > Height:
            self.y = 0

    def draw_snake(self, window):
        for block in self.snake_list:
            pygame.draw.rect(window, self.color, (block[0], block[1], self.width, self.height))

# Food Class
class Food:
    def __init__(self, size):
        self.size = size
        self.x = random.randint(20, Width - 20)
        self.y = random.randint(20, Height - 20)

    def draw_food(self, window, color):
        pygame.draw.circle(window, color, (self.x, self.y), self.size)

# Objects
Mr_Snake = Python(400, 250, 15, 15, 7, "RIGHT", (0, 0, 255))
Guinea_pig = Food(8)

# Colors
Background = (13, 17, 100)
Guinea_pig_colour = (255, 225, 0)

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Mr_Snake.change_direction("UP")
            elif event.key == pygame.K_s:
                Mr_Snake.change_direction("DOWN")
            elif event.key == pygame.K_a:
                Mr_Snake.change_direction("LEFT")
            elif event.key == pygame.K_d:
                Mr_Snake.change_direction("RIGHT")

    Mr_Snake.move_snake()
    Mr_Snake.check_borders()

    # Snake body management
    Mr_Snake.snake_list.append([Mr_Snake.x, Mr_Snake.y])
    if len(Mr_Snake.snake_list) > Mr_Snake.snake_length:
        del Mr_Snake.snake_list[0]

    # Fill screen
    Window.fill(Background)

    # Draw food
    Guinea_pig.draw_food(Window, Guinea_pig_colour)

    # Draw snake
    Mr_Snake.draw_snake(Window)

    # Collision check (simple distance check)
    snake_head = pygame.Rect(Mr_Snake.x, Mr_Snake.y, Mr_Snake.width, Mr_Snake.height)
    food_rect = pygame.Rect(Guinea_pig.x - Guinea_pig.size, Guinea_pig.y - Guinea_pig.size, Guinea_pig.size * 2, Guinea_pig.size * 2)

    if snake_head.colliderect(food_rect):
        print("Collide!")
        Mr_Snake.snake_length += 5
        Guinea_pig = Food(8)  # new food

    # Refresh
    pygame.display.update()
    Clock.tick(30)

pygame.quit()
