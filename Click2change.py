import pygame

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width,Height))
Title = pygame.display.set_caption(" Change The Title")
Clock = pygame.time.Clock()
run = True
# colors
Window_color = (11, 29, 81)
button1_color = (9, 63, 180)
button2_color = (237, 53, 0)
button_color = button1_color

# Button 1 and 2
rect_width = 125
rect_height = 75
rect_x = Width // 2 - 100
rect_y = Height // 2
rect_2 = pygame.Rect(rect_x,rect_y,rect_width,rect_height)
rect_1 = pygame.Rect(rect_x,rect_y,rect_width,rect_height)

# Window
while run :
# Mouse Hover Stuff
    mouse_x,mouse_y = pygame.mouse.get_pos()
    if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
        button_color = button2_color
    else:
        button_color = button1_color



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.collidepoint(event.pos):
                button_color = button2_color

# Fill
    Window.fill(Window_color)
# Draw
    pygame.draw.rect(Window,(button_color),rect_1)
# Refresh
    pygame.display.flip()
# Delay
    Clock.tick(30)
pygame.quit()