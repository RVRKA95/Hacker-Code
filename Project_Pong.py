import pygame

pygame.init()

Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("PROJECT_PONG")
Green = (31, 125, 83)
White = (251, 251, 251)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

left_paddle_x = 30
left_paddle_y = 200
right_paddle_x = 755
right_paddle_y = 200
paddle_width = 20
paddle_height = 100
ball_x = Width // 2
ball_y = Height // 2 
ball_size = 10
paddle_speed = 10  
ball_speed_x = 6
ball_speed_y = 6

left_score = 0
right_score = 0

left_change_y = 0
right_change_y = 0


trail = []

run = True
while run:
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

    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > Height - paddle_height:
        left_paddle_y = Height - paddle_height
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > Height - paddle_height:
        right_paddle_y = Height - paddle_height

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= Height - ball_size:
        ball_speed_y *= -1

    # Ball collision with left paddle
    if (
        ball_x <= left_paddle_x + paddle_width and
        left_paddle_y <= ball_y <= left_paddle_y + paddle_height
    ):
        ball_speed_x *= -1

    # Ball collision with right paddle
    if (
        ball_x >= right_paddle_x - paddle_width and
        right_paddle_y <= ball_y <= right_paddle_y + paddle_height
    ):
        ball_speed_x *= -1

    if ball_x - ball_size < 0:
        right_score += 1
        ball_x = Width // 2
        ball_y = Height // 2
        ball_speed_x = -ball_speed_x
    if ball_x + ball_size > Width:
        left_score += 1
        ball_x = Width // 2
        ball_y = Height // 2
        ball_speed_x = -ball_speed_x

    trail.append((ball_x, ball_y))
    if len(trail) > 9:  
        trail.pop(0)

    Window.fill(Green)
    
  
    pygame.draw.line(Window, White, (Width // 2, 0), (Width // 2, Height), 2)
    
    pygame.draw.rect(Window, White, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(Window, White, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    

    for i, pos in enumerate(trail):
        alpha = int(255 * (i + 1) / len(trail))  # Calculate alpha value
        trail_color = (White[0], White[1], White[2], alpha)
        trail_surface = pygame.Surface((ball_size * 2, ball_size * 2), pygame.SRCALPHA)
        pygame.draw.circle(trail_surface, trail_color, (ball_size, ball_size), ball_size)
        Window.blit(trail_surface, (pos[0] - ball_size, pos[1] - ball_size))
    
  
    pygame.draw.circle(Window, White, (ball_x, ball_y), ball_size)

    left_score_text = font.render(str(left_score), True, White)
    right_score_text = font.render(str(right_score), True, White)
    Window.blit(left_score_text, (Width // 4, 20))
    Window.blit(right_score_text, (3 * Width // 4, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()