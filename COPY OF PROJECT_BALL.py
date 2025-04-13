import pygame
pygame.init()

Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("TESTING")
run = True
White = (255, 255, 255)
Green = (31, 125, 83)
font=pygame.font.Font(None, 60)  
right_paddle_x = 755
right_paddle_y = 200
left_paddle_x = 30
left_paddle_y = 200
paddle_width = 20  
paddle_height = 100
paddle_speed = 0.75
left_score=0
right_score=0

ball_x = 400
ball_y = 250
ball_radius = 10
ball_speed_x = 0.25
ball_speed_y = 0.25

left_change_y = 0
right_change_y = 0

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
    if ball_y - ball_radius < 0 or ball_y + ball_radius > Height:
        ball_speed_y *= -1
    if (
        ball_x - ball_radius < left_paddle_x + paddle_width and
        left_paddle_y < ball_y < left_paddle_y + paddle_height
    ):
        ball_speed_x *= -1
    if (
        ball_x + ball_radius > right_paddle_x and
        right_paddle_y < ball_y < right_paddle_y + paddle_height
    ):
        ball_speed_x *= -1
    if ball_x < 0 or ball_x > Width:
        ball_x = Width // 2
        ball_y = Height // 2
        ball_speed_x *= -1
        
    if ball_x <= 0:
        right_score += 1
        ball_x,ball_y =400,250
        ball_speed_x = -ball_speed_x
    if ball_x >= Width:
        left_score += 1
        ball_x,ball_y =400,250
        ball_speed_x = -ball_speed_x
    

    Window.fill(Green)
    pygame.draw.rect(Window, White, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(Window, White, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.line(Window, White, (400, 0), (400, 500), 5)
    pygame.draw.circle(Window, White, (ball_x, ball_y), ball_radius)
    left_score_text = font.render(str(left_score), True, White)
    right_score_text = font.render(str(right_score), True, White)
    Window.blit(left_score_text, (175, 10))
    Window.blit(right_score_text, (615, 10))
    pygame.display.update()

pygame.quit()

