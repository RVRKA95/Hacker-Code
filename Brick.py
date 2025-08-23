import pygame

pygame.init()

# Window_settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Change The Title")
End_text = pygame.font.Font(None,60)
Text = pygame.font.Font(None,50)
Clock = pygame.time.Clock()

# Colors
Window_color = (0,0,0)
Ball_color = (255,255,255)
Paddle_color = (255,255,255)
Brick_color = (255,255,255)
Text_color = (255,255,255)

# Paddle_settings
paddle_width = 100
paddle_height = 15
paddle_x = 350
paddle_y = 475
paddle_change = 0
paddle_speed = 7
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# Ball_settings
ball_radius = 7
ball_x = 400
ball_y = 450
ball_speed_x = 5
ball_speed_y = -5
ball = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)

# Brick_settings
brick_width = 120
brick_height = 40
brick_row = 6
brick_coloum = 6
start_x = 30
start_y = 50
brick_gap = 5
bricks = []

# Brick_logic
for row in range(brick_row):
    for coloum in range(brick_coloum):
        x = start_x + coloum * (brick_width + brick_gap)
        y = start_y + row * (brick_height + brick_gap)
        brick = pygame.Rect(x, y, brick_width, brick_height)
        bricks.append(brick) 

# Lives
Lives = 5

# Score
Score = 0

# Game over = True/False
Game_over = False

# Win = True / False
Victory = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not Game_over and not Victory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paddle_change = -paddle_speed
                if event.key == pygame.K_d:
                    paddle_change = paddle_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    paddle_change = 0
        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                run = False

    if not Game_over and not Victory:
        # Paddle_logic
        paddle_x += paddle_change
        paddle_x = max(0, min(Width - paddle_width, paddle_x))
        paddle.x = paddle_x
        paddle.y = paddle_y

        # Ball_logic
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        if ball_x <= 0 or ball_x >= Width - ball_radius * 2:
            ball_speed_x *= -1
        if ball_y <= 0:
            ball_speed_y *= -1
        if ball_y >= Height - ball_radius * 2:
            ball_x = Width // 2
            ball_y = Height // 2
            Lives -= 1
            if Lives <= 0:
                Game_over = True
        ball.x = ball_x
        ball.y = ball_y

        # Collision 
        if ball.colliderect(paddle):
            ball_speed_y *= -1

        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_speed_y *= -1
                Score += 10
                break

        # Fill
        Window.fill(Window_color)

        # Draw
        pygame.draw.rect(Window, Paddle_color, paddle)
        pygame.draw.ellipse(Window, Ball_color, ball)
        for brick in bricks:
            pygame.draw.rect(Window, Brick_color, brick)

        # Blit 
        score_text = Text.render(f"Score: {Score}", True, Text_color)
        lives_text = Text.render(f"Lives: {Lives}", True, Text_color)
        Window.blit(score_text, (10, 10))
        Window.blit(lives_text, (Width - 150, 10))

    elif Game_over:
        # Game Over
        Window.fill(Window_color)
        Game_over_text = End_text.render("Game Over! Press Any Key To Quit!",True,(255,255,255))
        Final_score_text = Text.render(f"Final Score Was {Score}",True,(255,255,255))
        Window.blit(Game_over_text,(Width // 2 - 350, Height // 2 - 20))
        Window.blit(Final_score_text,(Width // 2 - 180,Height // 2 + 45))
    else:
        # Victory
        Window.fill(Window_color)
        Victory_text = End_text.render("You Win! Press Any Key To Quit!", True, (255, 255, 255))
        Final_score_text = Text.render(f"Final Score Was {Score}", True, (255, 255, 255))
        Window.blit(Victory_text, (Width // 2 - 350, Height // 2 - 20))
        Window.blit(Final_score_text, (Width // 2 - 180, Height // 2 + 45))
    # Refresh
    pygame.display.update()
    # Delay
    Clock.tick(60)
# Quit
pygame.quit()