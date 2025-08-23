import pygame
import random

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Ball")
Clock = pygame.time.Clock() 
# Music = pygame.mixer.Sound(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Music\2019-01-02_-_8_Bit_Menu_-_David_Renda_-_FesliyanStudios.com.mp3")
Hit = pygame.mixer.Sound(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Music\flappy-bird-hit-sound-101soundboards.mp3")
run = True

# Ball 
ball_x = 50    
ball_y = 250
ball_width = 30   
ball_height = 30
jump_strength = -8
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)

# Physics
gravity = 0.5
velocity = 0    

# Pipe
pipe_width = 70
pipe_gap = 150
pipe_x = Width
pipe_height = random.randint(100, 400)
pipe_speed = 3

Top_paddle = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
Down_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, Height - pipe_height - pipe_gap)

# Colors
Ball_color = (251, 65, 65)
pipe_color = (120, 200, 65)
BG_color = (26, 42, 128)

# Lives
Lives = 3

# Music.play(-1)  BG Music
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = jump_strength

    # Movement
    velocity += gravity
    ball_y += velocity
    ball.topleft = (ball_x, int(ball_y))

    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = Width
        pipe_height = random.randint(100, 400)
    Top_paddle = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    Down_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, Height - pipe_height - pipe_gap)

    # Collision
    if ball.colliderect(Top_paddle):
        Hit.play()
        Lives -= 1

    if ball.colliderect(Down_pipe):
        Hit.play()
        Lives -= 1

    if ball_y < 0 or ball_y > Height - ball_height:
        Hit.play()
        pygame.time.delay(103)
        pygame.display.update()
        Lives -= 1
    

# Life Check
    if Lives <= 0:
        run = False

    # Fill
    Window.fill(BG_color)
    # Draw
    pygame.draw.ellipse(Window, Ball_color, ball)
    pygame.draw.rect(Window, pipe_color, Top_paddle)
    pygame.draw.rect(Window, pipe_color, Down_pipe)
    # Delay
    Clock.tick(30)
    # Refresh
    pygame.display.update()
# Quit
pygame.quit()