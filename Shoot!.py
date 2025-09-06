import pygame
import random
import pygame.mixer
  
pygame.init()
pygame.mixer.init()

# Window creation
Width = 800
Height = 500
Window = pygame.display.set_mode((Width,Height))
Title = pygame.display.set_caption("Shoot!")
# Variables for code
Clock = pygame.time.Clock()
Text = pygame.font.Font(None, 75)
Music = pygame.mixer.Sound(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Code\shoot.wav")

# Player Settings
paddle_width = 100
paddle_height = 15
paddle_x = Width //2 - paddle_width
paddle_y =  Height - 50
paddle_speed = 7
change = 0
# colors
Window_color = (11, 29, 81)
paddle_color =(152, 205, 0)
enemy_color = (175, 62, 62)
# Bullet Settings
bullet_radius = 3
bullet_speed = 5
bullets = []
fire_bullet = False
# Enemy Settings
enemy_x = random.randint(0, Width - paddle_width)
enemy_y = 0
enemy_speed = 3
enemy_width = 75
enemy_height = 15
# Scores
score = 0

# Window 
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                change -= paddle_speed
            if event.key == pygame.K_d:
                change += paddle_speed
            if event.key == pygame.K_SPACE:
                bullet_x = paddle_x + paddle_width // 2
                bullet_y = paddle_y
                bullets.append([bullet_x, bullet_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                change = 0
# Movement 
    enemy_y += enemy_speed
    paddle_x += change
# Borders
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > Width - paddle_width:
        paddle_x = Width - paddle_width
                
    if enemy_y > Height:
        enemy_x = random.randint(0, Width - enemy_width)
        enemy_y = 0
        enemy_speed -= 0.1
        if enemy_speed < 3:
            enemy_speed = 3
        score -= 1

# Score Check
     if score <= 0:
       score = 0

# Bullet Logic
    if fire_bullet:
        bullet_x = paddle_x + paddle_width // 2
        bullet_y = paddle_y
        bullets.append([bullet_x, bullet_y])
        fire_bullet = False
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed  
        if bullet[1] < 0:
            bullets.remove(bullet)

# Collision Detection And Difficulty Increase
    for bullet in bullets[:]:
        if (enemy_x < bullet[0] < enemy_x + enemy_width) and \
        (enemy_y < bullet[1] < enemy_y + enemy_height):
            bullets.remove(bullet)
            Music.play()
            enemy_speed += 0.1
            score += 1
            enemy_x = random.randint(0, Width - enemy_width)
            enemy_y = 0
# Refresh , Fill and Draw

# Fill
    Window.fill(Window_color)
# Draw
    pygame.draw.rect(Window, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(Window, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))
    for bullet in bullets:
        pygame.draw.circle(Window, (255, 255, 255), (bullet[0], bullet[1]), bullet_radius)
# Blit
    Score_text = Text.render(f"{score}", True, (255, 255, 255))
    Window.blit(Score_text, (375,10))
# Refresh
    pygame.display.update()
    
    Clock.tick(60)
pygame.quit()

