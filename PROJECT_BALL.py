import pygame
import random

pygame.init()

# set up the window
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("Bouncy Ball!")

# colors
Colour = [(255, 0, 0), (143, 135, 241), (198, 142, 253), (254, 210, 226)]
White = (253, 250, 246)

# ball properties
ball_number = 6
balls = []  # Define the balls list

for _ in range(ball_number):
    ball_radius = 30
    ball_x = random.randint(ball_radius, Width - ball_radius)
    ball_y = random.randint(ball_radius, Height - ball_radius)
    ball_speed_x = random.choice([-10, 10])
    ball_speed_y = random.choice([-10, 10])
    ball_colour = random.choice(Colour)
    balls.append({
        "x": ball_x,
        "y": ball_y,
        "speed_x": ball_speed_x,
        "speed_y": ball_speed_y,
        "radius": ball_radius,
        "colour": ball_colour
    })
Clock=pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the window with white color
    Window.fill(White)
    # update ball positions and draw them
    for ball in balls:
        ball["x"] += ball["speed_x"]
        ball["y"] += ball["speed_y"]

        # check for collision with walls
        if ball["x"] - ball["radius"] < 0 or ball["x"] + ball["radius"] > Width:
            ball["speed_x"] *= -1
        if ball["y"] - ball["radius"] < 0 or ball["y"] + ball["radius"] > Height:
            ball["speed_y"] *= -1

        
        pygame.draw.circle(Window, ball["colour"], (ball["x"], ball["y"]), ball["radius"])

    pygame.display.update()
    Clock.tick(60)

pygame.quit()