import pygame
import time
pygame.init()

Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("CLICK 2.0")
font= pygame.font.Font(None, 30)
score_font=pygame.font.Font(None,55)
over_font=pygame.font.Font(None,75)
Green = (103, 174, 110)
White = (239, 238, 234)
TXT_Colour = (57, 62, 70)
box_width = 115
box_height = 75
box_x = (Width - box_width) // 2
box_y = (Height - box_height) // 1.9
score=0 
game_duration=10
start_time=time.time()
Window.fill(Green)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN and remaining_time > 0 :
            mouse_x,mouse_y= event.pos
            if ((box_x <= mouse_x <= box_x + box_width) and (box_y <= mouse_y <= box_y +box_height)):
                score+=1    
    Elapsed=int(time.time()-start_time) 
    remaining_time=game_duration-Elapsed
    if remaining_time<0:
        remaining_time=0 
    Window.fill(Green)
    pygame.draw.rect(Window, White, (box_x, box_y, box_width, box_height))
    Click=font.render("CLICK ME!", True, TXT_Colour )
    Window.blit(Click, (box_x+5,box_y+25))
    scores=score_font.render(f"Score : {score}",True,TXT_Colour)
    Window.blit(scores,(15,15))
    timer_text=score_font.render(f"Time Left : {remaining_time}",True,TXT_Colour)
    Window.blit(timer_text,(15,75)) 
    if remaining_time == 0:
        over_text=over_font.render("Time's Up!",True,TXT_Colour)
        Window.blit(over_text,(box_x-50,int(box_y+150)))
  
    pygame.display.update()   

pygame.quit() 