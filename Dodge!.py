# import pygame
# import random
  
# pygame.init()

# # Window creation
# Width, Height = 800, 500
# Window = pygame.display.set_mode((Width, Height))
# pygame.display.set_caption("Dodge!")

# # Variables
# Clock = pygame.time.Clock()
# Font = pygame.font.Font(None, 75)
# Game_Over = False

# # Player Settings
# player_width, player_height = 50,50
# player_x = Width // 2 - player_width
# player_y = Height - 55
# player_speed = 7
# change = 0

# # Colors
# Window_color = (11, 29, 81)
# player_color = (220, 20, 60)
# enemy_color = (155, 93, 224)

# # Enemy Settings
# enemy_width, enemy_height = 50,50
# enemy_x = random.randint(0, Width - enemy_width)
# enemy_y = 0
# enemy_speed = 3

# # Score
# score = 0

# # Game Loop
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if not Game_Over:  
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_a:
#                     change = -player_speed
#                 if event.key == pygame.K_d:
#                     change = player_speed
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_a or pygame.K_d:
#                     change = 0

#     if not Game_Over:
#         # Movement
#         player_x += change
#         enemy_y += enemy_speed

#         # Borders
#         if player_x < 0:
#             player_x = 0
#         if player_x > Width - player_width:
#             player_x = Width - player_width 

#         # Reset enemy when off screen
#         if enemy_y > Height:
#             enemy_x = random.randint(0, Width - enemy_width)
#             enemy_y = 0
#             score += 1
#             enemy_speed += 1

#         # Rects for collision
#         Player = pygame.Rect(player_x, player_y, player_width, player_height)
#         Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

#         # Collision check
#         if Player.colliderect(Enemy):
#             Game_Over = True
#         # Score Check
#         if score <= 0:
#             score = 0

#     # Drawing
#     Window.fill(Window_color)

#     if Game_Over:
#         over_txt = Font.render("Game Over!", True, (255, 255, 255))
#         Window.blit(over_txt, (250,220))  
#     else:
#         pygame.draw.rect(Window, player_color, Player)
#         pygame.draw.rect(Window, enemy_color, Enemy)
#         score_txt = Font.render(f"{score}", True, (255, 255, 255))
#         Window.blit(score_txt, (10, 10))

#     pygame.display.update()
#     Clock.tick(60)

# pygame.quit()

# //////////////////////////////////////////////////////// Lives //////////////////////////////////////////////////////////////
# import pygame
# import random
  
# pygame.init()

# # Window creation
# Width, Height = 800, 500
# Window = pygame.display.set_mode((Width, Height))
# pygame.display.set_caption("Dodge!")

# # Variables
# Clock = pygame.time.Clock()
# Font = pygame.font.Font(None, 60)
# Game_Over = False
# Lives = 3

# # Player Settings
# player_width, player_height = 50, 50
# player_x = Width // 2 - player_width // 2
# player_y = Height - 60
# player_speed = 7
# change = 0

# # Colors
# Window_color = (11, 29, 81)
# player_color = (220, 20, 60)
# enemy_color = (155, 93, 224)

# # Enemy Settings
# enemy_width, enemy_height = 50, 50
# enemy_x = random.randint(0, Width - enemy_width)
# enemy_y = 0
# enemy_speed = 3

# # Score
# score = 0

# # Game Loop
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if not Game_Over:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_a:
#                     change = -player_speed
#                 if event.key == pygame.K_d:
#                     change = player_speed
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_a or pygame.K_d:
#                     change = 0

#     if not Game_Over:
#         # Movement
#         player_x += change
#         enemy_y += enemy_speed

#         # Borders
#         player_x = max(0, min(player_x, Width - player_width))

#         # Reset enemy when off screen
#         if enemy_y > Height:
#             enemy_x = random.randint(0, Width - enemy_width)
#             enemy_y = 0
#             score += 1
#             enemy_speed += 0.2

#         # Rects for collision
#         Player = pygame.Rect(player_x, player_y, player_width, player_height)
#         Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

#         # Collision check
#         if Player.colliderect(Enemy):
#             Lives -= 1
#             enemy_x = random.randint(0, Width - enemy_width)
#             enemy_y = 0
#             if Lives <= 0:
#                 Game_Over = True

#     # Drawing
#     Window.fill(Window_color)

#     if Game_Over:
#         over_txt = Font.render("Game Over!", True, (255, 255, 255))
#         score_txt = Font.render(f"Score: {score}", True, (255, 255, 255))
#         Window.blit(over_txt, (Width//2 - 150, Height//2 - 50))
#         Window.blit(score_txt, (Width//2 - 100, Height//2 + 20))
#     else:
#         pygame.draw.rect(Window, player_color, Player)
#         pygame.draw.rect(Window, enemy_color, Enemy)

#         score_txt = Font.render(f"Score: {score}", True, (255, 255, 255))
#         lives_txt = Font.render(f"Lives: {Lives}", True, (255, 255, 255))

#         Window.blit(score_txt, (10, 10))
#         Window.blit(lives_txt, (Width - 200, 10))

#     pygame.display.update()
#     Clock.tick(60)

# pygame.quit()

# # //////////////////////////////////////////// Steal Truck Truck Drive! //////////////////////////////////////////////////////////
# import pygame
# import random
  
# pygame.init()

# # Window creation
# Width, Height = 800, 500
# Window = pygame.display.set_mode((Width, Height))
# pygame.display.set_caption("Dodge!")

# # Variables
# Clock = pygame.time.Clock()
# Font = pygame.font.Font(None, 75)
# Game_Over = False

# # Player Settings
# player_x = Width // 2 
# player_y = Height - 140
# player_speed = 7
# change = 0

# # Enemy Settings
# enemy_x = random.randint(0, Width - 70)
# enemy_y = 0
# enemy_speed = 4

# # Images 
# Player = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Images\Red_SPORT_CLEAN_All_036.png")
# Enemy = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Images\Green_PICKUP_CLEAN_All_012.png")
# BackGround = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Images\Road.jpg")
# crash = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Images\cRASH.png")

# # Transform (scale)
# Player = pygame.transform.scale(Player, (100,125))
# Enemy = pygame.transform.scale(Enemy, (100,125))
# crash = pygame.transform.scale(crash,(100,125))
# BackGround = pygame.transform.scale(BackGround, (Width, Height))
# # Music
# Crash = pygame.mixer.Sound(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Music\explosion-8-bit-11-314691.mp3")

# # Score
# score = 0

# # Game Loop
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if not Game_Over:  
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_a:
#                     change = -player_speed
#                 if event.key == pygame.K_d:
#                     change = player_speed
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_a or pygame.K_d:
#                     change = 0

#     if not Game_Over:
#         # Movement
#         player_x += change
#         enemy_y += enemy_speed

#         # Borders
#         if player_x < 0:
#             player_x = 0
#         if player_x > Width - 100:
#             player_x = Width - 100

#         # Reset enemy when off screen
#         if enemy_y > Height:
#             enemy_x = random.randint(0, Width - 70)
#             enemy_y = -120

#         # Collision check (increase score when crash)
#         player_rect = pygame.Rect(player_x, player_y, 100, 125)
#         enemy_rect = pygame.Rect(enemy_x, enemy_y, 100,125)
#         if player_rect.colliderect(enemy_rect):
#             # Play sound
#             Crash.play()
#             # Show crash immediately
#             Window.blit(BackGround, (0, 0))
#             Window.blit(Player, (player_x, player_y))
#             Window.blit(crash,(enemy_x,enemy_y))
#             # pygame.display.update()


#             # Increase score and reset
#             score += 1
#             enemy_x = random.randint(0, Width - 70)
#             enemy_y = -120  

#     # Drawing
#     Window.blit(BackGround, (0, 0))
#     Window.blit(Player, (player_x, player_y))
#     Window.blit(Enemy, (enemy_x, enemy_y))
#     score_txt = Font.render(f"{score}", True, (255, 255, 255))
#     Window.blit(score_txt, (10, 10))

#     pygame.display.update()
#     Clock.tick(60)

# pygame.quit()

# ////////////////////////////// Screens //////////////////////////////

# import pygame
# import random
  
# pygame.init()

# # Window creation
# Width, Height = 800, 500
# Window = pygame.display.set_mode((Width, Height))
# pygame.display.set_caption("Dodge!")

# # Variables
# Clock = pygame.time.Clock()
# Font = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 75)
# Title = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 150)
# Retry = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 50)

# # Colors
# Window_color = (11, 29, 81)
# player_color = (220, 20, 60)
# enemy_color = (155, 93, 224)

# # Player Settings
# player_width, player_height = 50, 50
# player_x = Width // 2 - player_width // 2
# player_y = Height - 55
# player_speed = 7
# change = 0

# # Enemy Settings
# enemy_width, enemy_height = 50, 50
# enemy_x = random.randint(0, Width - enemy_width)
# enemy_y = 0
# enemy_speed = 3

# # States
# Start = True
# Game = False
# Game_Over = False

# # Level
# level = 1
# score = 0

# # Game Loop
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         # Start Screen
#         if Start:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_e:
#                     Start = False
#                     Game = True
#                     Game_Over = False
#                     score = 0
#                     enemy_speed = 3
#                     enemy_y = 0
#                     enemy_x = random.randint(0, Width - enemy_width)

#         # Keys
#         elif Game and not Game_Over:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_a:
#                     change = -player_speed
#                 if event.key == pygame.K_d:
#                     change = player_speed
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_a or pygame.K_d:
#                     change = 0

#         # Game Over Screen
#         elif Game_Over:
#             if event.type == pygame.KEYDOWN:
#              if event.key == pygame.K_r:
#                 Game_Over = False
#                 Game = True
#                 score = 0
#                 enemy_speed = 3
#                 enemy_y = 0
#                 enemy_x = random.randint(0, Width - enemy_width)

#     # Logic
#     if Game and not Game_Over:
#         player_x += change
#         enemy_y += enemy_speed

#         # Borders
#         if player_x < 0:
#             player_x = 0
#         if player_x > Width - player_width:
#             player_x = Width - player_width 

#         # Enemy reset when off screen
#         if enemy_y > Height:
#             enemy_x = random.randint(0, Width - enemy_width)
#             enemy_y = 0
#             score += 1
#             enemy_speed = 5

#         # Collision
#         Player = pygame.Rect(player_x, player_y, player_width, player_height)
#         Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
#         if Player.colliderect(Enemy):
#             Game_Over = True

#         # Leveling logic 
#         if score >= 50:
#             level = 4
#             enemy_speed = 6
#         elif score >= 30:
#             level = 3
#             enemy_speed = 5.5
#         elif score >= 5:
#             level = 2
#             enemy_speed = 5
#         else:
#             level = 1  
#     # Draw
#     Window.fill(Window_color)

#     if Start:
#         title_text = Title.render(" $ Dodge $", True, (255, 255, 255))
#         enter_text = Retry.render("Press E to Ignite", True, (255, 0, 0))
#         Window.blit(title_text, (50, 150))
#         Window.blit(enter_text, (240, 300))

#     elif Game and not Game_Over:
#         Player = pygame.Rect(player_x, player_y, player_width, player_height)
#         Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
#         pygame.draw.rect(Window, player_color, Player)
#         pygame.draw.rect(Window, enemy_color, Enemy)
#         score_txt = Font.render(f"{score}", True, (255, 255, 255))
#         lvl_text = Font.render(f"{level}", True, (255, 0, 0))
#         Window.blit(score_txt, (10, 10))
#         Window.blit(lvl_text, (760, 10))

#     elif Game_Over:
#         level = 1
#         score = 0
#         over_txt = Title.render("Derailed!", True, (255, 255, 255))
#         retry_txt = Retry.render("Press R to Reignite", True, (255, 0, 0))
#         Window.blit(over_txt, (150, 150))
#         Window.blit(retry_txt, (230, 300))

#     pygame.display.update()
#     Clock.tick(30)

# pygame.quit()

#//////////////////////////// Walter's Lab ////////////////////////////////
import pygame
import random
  
pygame.init()

# Window creation
Width, Height = 800, 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Dodge!")

# Variables
Clock = pygame.time.Clock()
Font = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 75)
Title = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 150)
Retry = pygame.font.Font(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Fonts\Cipitillo.otf", 50)

# Colors
Window_color = (11, 29, 81)
player_color = (220, 20, 60)
enemy_color = (155, 93, 224)

# Player Settings
player_width, player_height = 50, 50
player_x = Width // 2 - player_width // 2
player_y = Height - 55
player_speed = 7
change = 0

# Enemy Settings
enemy_width, enemy_height = 50, 50
enemy_x = random.randint(0, Width - enemy_width)
enemy_y = 0
enemy_speed = 3

# States
Start = True
Game = False
Game_Over = False

# Level
level = 1
score = 0

# Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Start Screen
        if Start:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Start = False
                    Game = True
                    Game_Over = False
                    score = 0
                    enemy_speed = 3
                    enemy_y = 0
                    enemy_x = random.randint(0, Width - enemy_width)

        # Keys
        elif Game and not Game_Over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change = -player_speed
                if event.key == pygame.K_d:
                    change = player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or pygame.K_d:
                    change = 0

        # Game Over Screen
        elif Game_Over:
            if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                Game_Over = False
                Game = True
                score = 0
                enemy_speed = 3
                enemy_y = 0
                enemy_x = random.randint(0, Width - enemy_width)

    # Logic
    if Game and not Game_Over:
        player_x += change
        enemy_y += enemy_speed

        # Borders
        if player_x < 0:
            player_x = 0
        if player_x > Width - player_width:
            player_x = Width - player_width 

        # Enemy reset when off screen
        if enemy_y > Height:
            enemy_x = random.randint(0, Width - enemy_width)
            enemy_y = 0
            score += 1
            enemy_speed = 5

        # Collision
        Player = pygame.Rect(player_x, player_y, player_width, player_height)
        Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        if Player.colliderect(Enemy):
            Game_Over = True

        # Leveling logic 
        if score!= 0 and score % 10 == 0:
            level = score // 10 + 1
            enemy_speed = enemy_speed + level
    # Draw
    Window.fill(Window_color)

    if Start:
        title_text = Title.render(" $ Dodge $", True, (255, 255, 255))
        enter_text = Retry.render("Press E to Ignite", True, (255, 0, 0))
        Window.blit(title_text, (50, 150))
        Window.blit(enter_text, (240, 300))

    elif Game and not Game_Over:
        Player = pygame.Rect(player_x, player_y, player_width, player_height)
        Enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        pygame.draw.rect(Window, player_color, Player)
        pygame.draw.rect(Window, enemy_color, Enemy)
        score_txt = Font.render(f"{score}", True, (255, 255, 255))
        lvl_text = Font.render(f"{level}", True, (255, 0, 0))
        Window.blit(score_txt, (10, 10))
        Window.blit(lvl_text, (760, 10))

    elif Game_Over:
        level = 1
        score = 0
        over_txt = Title.render("Derailed!", True, (255, 255, 255))
        retry_txt = Retry.render("Press R to Reignite", True, (255, 0, 0))
        Window.blit(over_txt, (150, 150))
        Window.blit(retry_txt, (230, 300))

    pygame.display.update()
    Clock.tick(30)

pygame.quit()
