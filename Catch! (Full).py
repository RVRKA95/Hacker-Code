import pygame
import random
import os

pygame.init()

# Window setup
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("Catch!")
font = pygame.font.Font(None, 75)
high_font = pygame.font.Font(None, 50)
timer_font = pygame.font.Font(None, 50)
colour = (9, 18, 44)

# Ball properties
ball_radius = 25
ball_x = random.randint(ball_radius, Width - ball_radius)
ball_y = 0
ball_colour = (255, 11, 85)
ball_speed = 0.25

# Paddle properties
paddle_colour = (1, 24, 216)
paddle_x = Width // 2
paddle_y = Height - 50
paddle_width = 100
paddle_height = 25
paddle_speed = 1.50
paddle_change = 0

# Score and high score
score = 0
high_score_file = "HIGHSCORE.txt"
if os.path.exists(high_score_file):
    with open(high_score_file, "r") as file:
        high_score = int(file.read())
else:
    high_score = 0

# Timer
start_time = pygame.time.get_ticks()
game_duration = 120  # Game duration in seconds

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paddle_change = -paddle_speed
            if event.key == pygame.K_d:
                paddle_change = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                paddle_change = 0

    # Update paddle position
    paddle_x += paddle_change
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x + paddle_width > Width:
        paddle_x = Width - paddle_width

    # Update ball position
    ball_y += ball_speed


    # Reset ball if it goes off-screen
    if ball_y - ball_radius > Height:
        ball_y = 0
        ball_x = random.randint(ball_radius, Width - ball_radius)
        ball_speed += 0.1

    # Collision detection between ball and paddle
    if (
        paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height
        and paddle_x <= ball_x <= paddle_x + paddle_width
    ):
        score += 1
        ball_y = 0
        ball_x = random.randint(ball_radius, Width - ball_radius)

        # Update high score
        if score > high_score:
            high_score = score
            with open(high_score_file, "w") as file:
                file.write(str(high_score))

    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    # Stop the game when the timer reaches zero
    if elapsed_time >= game_duration:
        run = False

    # Fill the window with background color
    Window.fill(colour)

    # Draw the ball
    pygame.draw.circle(Window, ball_colour, (ball_x, ball_y), ball_radius)

    # Draw the paddle
    pygame.draw.rect(Window, paddle_colour, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Display the score
    score_text = font.render(f"{score}", True, (255, 255, 255))
    Window.blit(score_text, (Width // 2 - 50, 15))

    # Display the high score
    high_text = high_font.render(f"{high_score}", True, (255, 255, 255))
    Window.blit(high_text, (15, 15))

    # Display the timer
    timer_text = timer_font.render(f"{game_duration - elapsed_time}", True, (255, 255, 255))
    Window.blit(timer_text, (Width - 200, 15))

    # Update the display
    pygame.display.update()

pygame.quit()