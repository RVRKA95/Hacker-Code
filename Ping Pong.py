import pygame
import sys
import time

pygame.init()

Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("Ping Pong")
Green = (31, 125, 83)
White = (251, 251, 251)
Blue = (0, 0, 255)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
big_font = pygame.font.SysFont(None, 75)  # Larger font for blue scores

left_paddle_x = 30
left_paddle_y = 200
right_paddle_x = 755
right_paddle_y = 200
paddle_width = 20
paddle_height = 100
paddle_speed = 10

ball_x = Width // 2
ball_y = Height // 2
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

left_score = 0
right_score = 0

left_change_y = 0
right_change_y = 0

start_time = time.time()
run = True
while run:
    elapsed_time = time.time() - start_time
    remaining_time = max(0, 60 - int(elapsed_time))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_change_y = -paddle_speed
            if event.key == pygame.K_s:
                left_change_y = paddle_speed
            if event.key == pygame.K_UP:
                right_change_y = -paddle_speed
            if event.key == pygame.K_DOWN:
                right_change_y = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_change_y = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_change_y = 0

    left_paddle_y += left_change_y
    right_paddle_y += right_change_y

    # Boundary checks for left paddle
    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > Height - paddle_height:
        left_paddle_y = Height - paddle_height

    # Boundary checks for right paddle
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > Height - paddle_height:
        right_paddle_y = Height - paddle_height

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y - ball_radius < 0 or ball_y + ball_radius > Height:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (ball_x - ball_radius < left_paddle_x + paddle_width and
        left_paddle_y < ball_y < left_paddle_y + paddle_height):
        ball_speed_x = -ball_speed_x
    if (ball_x + ball_radius > right_paddle_x and
        right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # Ball collision with left and right walls (reset ball position and update score)
    if ball_x - ball_radius < 0:
        right_score += 1
        ball_x = Width // 2
        ball_y = Height // 2
        ball_speed_x = -ball_speed_x
    if ball_x + ball_radius > Width:
        left_score += 1
        ball_x = Width // 2
        ball_y = Height // 2
        ball_speed_x = -ball_speed_x

    Window.fill(Green)
    
    # Draw the middle line
    pygame.draw.line(Window, White, (Width // 2, 0), (Width // 2, Height), 2)
    
    pygame.draw.rect(Window, White, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(Window, White, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(Window, White, (ball_x, ball_y), ball_radius)

    # Render the scores
    left_score_color = Blue if left_score > right_score else White
    right_score_color = Blue if right_score > left_score else White
    left_score_font = big_font if left_score > right_score else font
    right_score_font = big_font if right_score > left_score else font
    left_score_text = left_score_font.render(str(left_score), True, left_score_color)
    right_score_text = right_score_font.render(str(right_score), True, right_score_color)
    Window.blit(left_score_text, (Width // 4, 20))
    Window.blit(right_score_text, (3 * Width // 4, 20))

    # Render the timer in the top-right corner
    timer_text = font.render(str(remaining_time), True, White)
    Window.blit(timer_text, (Width - timer_text.get_width() - 20, 20))

    pygame.display.update()
    clock.tick(60)

    if remaining_time == 0:
        run = False

# Keep the window open for 10 seconds after the timer ends
end_time = time.time()
while time.time() - end_time < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()