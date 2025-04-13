import pygame

pygame.init()

Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("CLICK!")
font = pygame.font.SysFont(None, 60)
Green = (31, 125, 83)
Blue = (0, 0, 255)
White = (251, 251, 251)
SCORE = 0

rect_width = 139
rect_height = 75
rect_x = (Width - rect_width) // 2
rect_y = int((Height - rect_height) // 1.5)

run = True
while run:
    Window.fill(Green)
    score_text = font.render(f"{SCORE}", True, White)
    Window.blit(score_text, (Width // 2 - score_text.get_width() // 2, 20))
    
    button=pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    pygame.draw.rect(Window, Blue, button)
    Box = font.render("CLICK!", True, White)
    Window.blit(Box, (329,300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                SCORE=SCORE + 1




    pygame.display.update()

pygame.quit()

