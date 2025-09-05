from time import sleep

import pygame

pygame.init()
import requests
import time


timer = pygame.time.Clock()

width, height = 512, 364
GREY = (99, 99, 99)
GREY_BACK= (214, 214, 206)

font  = pygame.font.Font('PokemonFont.ttf', 10)

screen = pygame.display.set_mode((width, height))

messages_top = ["Hello there!","Welcome to the world of POKeMON!","My name is OAK.","People affectionately refer to me","This world..."]
active_message_top = 0
message_top = messages_top[active_message_top]

messages_bottom = ["Glad to meet you!","","","as the POKeMON PROFESSOR.",""]
active_message_bottom = 0
message_bottom = messages_bottom[active_message_bottom]


image = pygame.image.load('ProfOak.jpg').convert_alpha()
text_box = pygame.image.load('TextBox.png').convert_alpha()
image.set_alpha(0)
running = True

counter,counter2 = 0,0
done_top = False
done_bottom = False
speed = 1


def dropShadowText_Top(screen, text, size, x, y, c, s,  colour=(99, 99, 99), drop_colour=(214, 214, 206),  font=None ):

    dropshadow_offset = 2 + (size // 15)
    text_font = pygame.font.Font('PokemonFont.ttf', 10)



    text_bitmap = text_font.render(text[0:c//s], True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text[0:c//s], True, colour)
    screen.blit(text_bitmap, (x, y))

def dropShadowText_Bottom(screen, text, size, x, y, c, s,  colour=(99, 99, 99), drop_colour=(214, 214, 206),  font=None ):

    dropshadow_offset = 2 + (size // 15)
    text_font = pygame.font.Font('PokemonFont.ttf', 10)



    text_bitmap = text_font.render(text[0:c//s], True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text[0:c//s], True, colour)
    screen.blit(text_bitmap, (x, y))


while running:
    timer.tick(120)

    if counter < speed * len(message_top):
        counter += 1
        print(done_top)

    elif counter >= speed * len(message_top):
        done_top = True

    if done_top == True:
        if counter2 < speed * len(message_bottom):
            counter2 += 1
            print(counter2)

        elif counter2 >= speed * len(message_bottom):
            done_bottom = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                active_message_top += 1
                active_message_bottom += 1

                done_top = False

                message_top = messages_top[active_message_top]
                message_bottom = messages_bottom[active_message_bottom]


                counter = 0
                counter2 = 0





    screen.blit(image, (0, 0))
    screen.blit(text_box, (0, 270))

    dropShadowText_Top(screen,message_top, 10, 36, 287, counter, speed)
    dropShadowText_Bottom(screen,message_bottom, 10, 36, 314, counter2, speed)

    pygame.display.update()



    for x in range(128):
        image.set_alpha(x)
        pygame.time.delay(1)



    pygame.display.update()

