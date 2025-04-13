import pygame
import random

pygame.init()
# Set Up Window
Width=800
Height=500
Window=pygame.display.set_mode((Width,Height))
Title=pygame.display.set_caption("1_BALL!")
# Variables
ball_numbers=6
Window_colour=(18, 52, 88)
colours=[(198, 142, 253),(143, 135, 241),(254, 210, 226),(115, 92, 221)]
Window_colour=(Window_colour)
ball_colour=random.choice(colours)
balls=[]
for _ in range(ball_numbers):
    ball_radius=25
    ball_x=random.randint(ball_radius,Width-ball_radius)
    ball_y=random.randint(ball_radius,Height-ball_radius)
    ball_speed_x=random.choice([10, -10])
    ball_speed_y=random.choice([10, -10])
    ball_colour=random.choice(colours)
    balls.append({
      "x":ball_x,
      "y":ball_y,
      "radius":ball_radius,
      "speed_x":ball_speed_x,
      "speed_y":ball_speed_y,
      "colour":ball_colour,

    })
Clock=pygame.time.Clock()

# Game Loop
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    # Update Ball Position
    for ball in balls:
        ball["x"]+= ball["speed_x"]
        ball["y"]+= ball["speed_y"]
        # Check for Collision with Walls
        if ball["x"] - ball["radius"]< 0 or ball["x"] + ball["radius"] > Width:
            ball["speed_x"] *= -1
        if ball["y"] - ball["radius"] < 0 or ball["y"] + ball["radius"] > Height:
            ball["speed_y"] *= -1
    # Fill the Window With Color
    Window.fill(Window_colour)  
    # Draw the Ball
    for ball in balls:
       pygame.draw.circle(Window, ball["colour"], (ball["x"],ball["y"]), ball["radius"])
    Clock.tick(120)
    pygame.display.update()

pygame.quit()