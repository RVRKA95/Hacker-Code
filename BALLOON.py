import pygame
import random
import time
pygame.init()
pygame.mixer.init()

Width = 800
height = 500
Window = pygame.display.set_mode((Width, height))
pygame.display.set_caption("BALLOON")
Clock = pygame.time.Clock()
Pop = pygame.mixer.Sound(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Code\pop-cartoon-328167 (1).mp3")
Font = pygame.font.Font(None, 75) 
Balloon_x = 400
Balloon_y = 475
Balloon_radius = 25
Balloon_speed = 5
Start_time=time.time()
Balloons = []
for _ in range(5):
    Balloon_x = random.randint(Balloon_radius, Width - Balloon_radius)
    Balloon_y = random.randint(height - 100, height - Balloon_radius)
    Balloons.append([Balloon_x, Balloon_y])

Score = 0
run = True

while run: 
    Window.fill((239, 238, 234))
    Game_Duration = 30
    Elapsed_Time = int(time.time() - Start_time)
    Remaining_time = Game_Duration - Elapsed_Time
    for i in range(len(Balloons)):
        Balloons[i][1] -= Balloon_speed
        pygame.draw.circle(Window, (255,0,0), (Balloons[i][0], Balloons[i][1]), Balloon_radius)
        if Balloons[i][1] < 0:
            Balloons[i][1] = height 
            Balloons[i][0] = random.randint(Balloon_radius, Width - Balloon_radius)
            
    if Remaining_time <= 0: 
        run = False 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    for i in range(len(Balloons)):
        Balloons[i][1],Balloons[i][1] - Balloon_speed


        if Balloons[i][1] < 0:
            Balloons[i][1] = height 

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i in range(len(Balloons)):
                Balloon_x,Balloon_y = Balloons[i]
                if Balloon_x - Balloon_radius <= mouse_x <= Balloon_x + Balloon_radius and \
                    Balloon_y - Balloon_radius <= mouse_y <= Balloon_y + Balloon_radius:
                    Pop.play()
                    Score += 1
                    Balloons[i][1] = height 
                    Balloons[i][0] = random.randint(Balloon_radius, Width - Balloon_radius)
    Score_Text = Font.render(f"{Score}", True, (39, 84, 138))
    Timer_Text = Font.render(f"{Remaining_time}", True, (39, 84, 138))
    Window.blit(Score_Text, (10,10))
    Window.blit(Timer_Text, (700, 10))
    pygame.display.update()
    Clock.tick(30) 

pygame.quit() 