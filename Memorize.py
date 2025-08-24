import pygame
import random

pygame.init()

# Window Settings
Width = 800
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Matching Madness!")
Clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
run = True

# Colors
BG_COLOR = (103, 174, 110)
Cards_facedown = (255, 144, 187)
Cards_faceup = (88, 160, 200)
Pair = (26, 42, 128)
Select_text = (255, 255, 255)

# Card grid settings
cols = 8
rows = 4
card_width = Width // cols
card_height = Height // rows
total_cards = cols * rows

# Values
numbers = (list(range(1, total_cards // 2 + 1))) * 2
random.shuffle(numbers)

# Game State
selected = []
matched = []
match_check_time = None

def draw_cards():
    Window.fill(BG_COLOR)
    for i, num in enumerate(numbers):
        x = (i % cols) * card_width
        y = (i // cols) * card_height
        rect = pygame.Rect(x, y, card_width, card_height)

        if i in matched:  # Matched
            pygame.draw.rect(Window, Pair, rect)
            text = font.render(str(num), True, Select_text)
            Window.blit(text, (x + card_width // 2 - 15, y + card_height // 2 - 15))
        elif i in selected:  # Selected
            pygame.draw.rect(Window, Cards_faceup, rect)
            text = font.render(str(num), True, Select_text)
            Window.blit(text, (x + card_width // 2 - 15, y + card_height // 2 - 15))
        else:  # Facedown
            pygame.draw.rect(Window, Cards_facedown, rect)
        pygame.draw.rect(Window, BG_COLOR, rect, 2)  # Border

while run:
    draw_cards()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(selected) < 2 and match_check_time is None:
                mx, my = pygame.mouse.get_pos()
                col = mx // card_width
                row = my // card_height
                idx = row * cols + col
                if idx not in selected and idx not in matched:
                    selected.append(idx)
                    if len(selected) == 2:
                        match_check_time = pygame.time.get_ticks()

    # Check for match after a short delay
    if match_check_time is not None:
        if pygame.time.get_ticks() - match_check_time > 1000:  # 1-second delay
            if numbers[selected[0]] == numbers[selected[1]]:
                matched.extend(selected)
            selected = []
            match_check_time = None

    # Reset cards if all matched
    if len(matched) == total_cards:
        pygame.time.delay(1000)  # Add a 1-second delay before resetting
        numbers = (list(range(1, total_cards // 2 + 1))) * 2
        random.shuffle(numbers)
        matched = []
        selected = []
        match_check_time = None
# Delay
    Clock.tick(30)
# Refresh
    pygame.display.flip()
# Quit
pygame.quit()