import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('Test.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


animation_list = []
animation_steps = [4,4,4,4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown =140
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter,17,24,3,BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:

    keys = pygame.key.get_pressed()

#update background
    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame+=1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

#show frame image

#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action != 0:
                action = 0
                frame = 0
            if event.key == pygame.K_UP and action != 1:
                action = 1
                frame = 0
            if event.key == pygame.K_LEFT and action != 2:
                action = 2
                frame = 0
            if event.key == pygame.K_RIGHT and action != 3:
                action = 3
                frame = 0

    if keys[pygame.K_UP]:
        action = 1
        screen.blit(animation_list[action][frame], (0, 0))
    elif keys[pygame.K_DOWN]:
        action = 0
        screen.blit(animation_list[action][frame], (0, 0))
    elif keys[pygame.K_LEFT]:
        action = 2
        screen.blit(animation_list[action][frame], (0, 0))
    elif keys[pygame.K_RIGHT]:
        action = 3
        screen.blit(animation_list[action][frame], (0, 0))
    else:
        screen.blit(animation_list[action][frame], (0, 0))
        frame = 0

    pygame.display.update()

pygame.quit()