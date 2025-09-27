import pygame
import random
import time

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Python.io")
Clock = pygame.time.Clock()
font = pygame.font.Font(None,50)
WHITE = (255,255,255)

tick_rate = 40
tick_change = tick_rate   # start with base speed

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
            elif event.key == pygame.K_UP:
                tick_change += 5   # speed up
            elif event.key == pygame.K_DOWN:
                tick_change -= 5   # slow down
                if tick_change < 5:   # prevent freezing
                    tick_change = 5

    Mr_Snake.move_snake()
    Mr_Snake.check_borders()

    # Fill screen
    Window.fill(Background)

    for x,y in Mr_Snake.snake_list:
        snake_box = pygame.draw.rect(Window, Mr_Snake.color,(x,y,Mr_Snake.width,Mr_Snake.height))
        food_box = pygame.draw.circle(Window, Guinea_pig_colour, (Guinea_pig.x, Guinea_pig.y), Guinea_pig.size)

        if snake_box.colliderect(pygame.Rect(Guinea_pig.x-Guinea_pig.size,
                                             Guinea_pig.y-Guinea_pig.size,
                                             Guinea_pig.size*2, Guinea_pig.size*2)):
            Guinea_pig = Food(8)
            Mr_Snake.snake_length += 3

    # Snake body management
    Mr_Snake.snake_list.append([Mr_Snake.x, Mr_Snake.y])
    if len(Mr_Snake.snake_list) > Mr_Snake.snake_length:
        Mr_Snake.snake_list.pop(0)
    if Mr_Snake.snake_list[-1] in Mr_Snake.snake_list[:-1]:
        time.sleep(2)
        Mr_Snake.snake_list.clear()
        Mr_Snake.snake_length = 1

    # Score
    screen_text = font.render(f"{Mr_Snake.snake_length - 1}", True, WHITE)
    Window.blit(screen_text, (10,10))

    # Refresh
    pygame.display.update()
    Clock.tick(tick_change)   # <- use tick_change here
    print(f"Current tick: {tick_change}")

pygame.quit()
