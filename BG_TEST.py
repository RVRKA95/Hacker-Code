import pygame

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width,Height))
Title = pygame.display.set_caption(" Change The Title")
Clock = pygame.time.Clock()
run = True

# Image Stuff
Image = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Tests\1.png")
image = pygame.transform.scale(Image,(50,50))
Image_2 = pygame.image.load(r"C:\Users\vihaa\OneDrive\Documents\Ultimate Code\Tests\2.png")
image_2 = pygame.transform.scale(Image_2,(50,50))

# Variables
rect_x = 375
rect_y = 250
rect = image.get_rect(topleft = (rect_x,rect_y))

# colors
Window_color = (11, 29, 81)

# Window
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# Mouse Stuff
    mouse_x,mouse_y = pygame.mouse.get_pos()
# Fill Stuff
    Window.fill(Window_color)
# Continue With Mouse Stuff

    if rect.collidepoint(mouse_x,mouse_y):
       Window.fill(Window_color)
       Window.blit(image,(rect_x,rect_y))
    else:
       Window.blit(image_2,(rect_x,rect_y))
    

# Refresh 
    pygame.display.update() 
# Delay
    Clock.tick(30)
pygame.quit()