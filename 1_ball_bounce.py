# Import
import pygame
import random

# Initialize Pygame
pygame.init()

# Window Settings
Width = 800
Height = 500

Window = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("1 Ball Bounce! ( Test ) :) ")

# Clock And Font
Clock = pygame.time.Clock()
Font = pygame.font.Font(None,50)

# Colors
Window_color = (17, 63, 103)

# Balls
balls = []
ball_radius = 25

for i in range(6):
    ball_x = random.randint(ball_radius, Width - ball_radius)
    ball_y = random.randint(ball_radius, Height - ball_radius)
    ball_speed_x = random.choice([10, -10])
    ball_speed_y = random.choice([10, -10])
    balls.append(
        {
            "x": ball_x,
            "y": ball_y,
            "speed_x": ball_speed_x,
            "speed_y": ball_speed_y,
            "color": random.choice([(234, 91, 111), (127, 85, 177), (244, 155, 171)])
        }
    )

# Window Creation 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    for ball in balls:
        ball["x"] += ball["speed_x"]
        ball["y"] += ball["speed_y"]

    # Collisions

        if ball["x"] < ball_radius or ball["x"] > Width - ball_radius:
            ball["speed_x"] *= -1
        if ball["y"] < ball_radius or ball["y"] > Height - ball_radius:
            ball["speed_y"] *= -1

    # Fill
    Window.fill(Window_color)
    # Draw
    for ball in balls:
        pygame.draw.circle(Window, ball["color"], (ball["x"], ball["y"]), ball_radius)
    # Refresh
    pygame.display.update()
    # Delay
    Clock.tick(60)
# Quit
pygame.quit()