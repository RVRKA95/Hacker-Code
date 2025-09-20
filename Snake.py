import pygame
import random

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snakes Galore!")
Clock = pygame.time.Clock()

# Snake
snake_width = 15
snake_height = 15
snake_x = 400
snake_y = 250
snake_speed = 7  
snake_change_x = 0   
snake_change_y = 0
Snake = pygame.Rect(snake_x, snake_y, snake_width, snake_height)
snake_color = (180, 229, 13)
# Food
Food_radius = 15
Food_x = random.randint(0, Width - Food_radius)
Food_y = random.randint(0, Height - Food_radius)
Food = pygame.Rect(Food_x, Food_y, Food_radius, Food_radius)
# colors
BG_COLOR = (26, 42, 128)
snake_color = (180, 229, 13)
food_color = (251, 65, 65)


# Window Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_change_y = -snake_speed
                snake_change_x = 0
            if event.key == pygame.K_s:  
                snake_change_y = snake_speed
                snake_change_x = 0
            if event.key == pygame.K_a: 
                snake_change_x = -snake_speed
                snake_change_y = 0
            if event.key == pygame.K_d:  
                snake_change_x = snake_speed
                snake_change_y = 0

    # Movement
    snake_x += snake_change_x
    snake_y += snake_change_y
    Snake.x = snake_x
    Snake.y = snake_y

    # Borders
    if Snake.x < 0:
        Snake.x = 0
    if Snake.x > Width - Snake.width:
        Snake.x = Width - Snake.width
    if Snake.y < 0:
        Snake.y = 0
    if Snake.y > Height - Snake.height:
        Snake.y = Height - Snake.height

    # Collision with food
    if Snake.colliderect(Food):
        Food.x = random.randint(0, Width - Food_radius)
        Food.y = random.randint(0, Height - Food_radius)

    # Fill screen
    Window.fill(BG_COLOR)  

    # Draw snake
    pygame.draw.rect(Window, snake_color, Snake)

    # Draw food
    pygame.draw.ellipse(Window, food_color, Food)


    # Refresh
    pygame.display.update()
    Clock.tick(30) 

# Quit
pygame.quit()
