import pygame
from time import sleep
from pyvidplayer import Video


pygame.init()
import requests
import time



width, height = 1024, 648
GREY = (99, 99, 99)
GREY_BACK= (214, 214, 206)


music = pygame.mixer.Sound("OakTheme.mp3")

font  = pygame.font.Font('PokemonFont.ttf', 90)

screen = pygame.display.set_mode((width, height))

messages_top = ["Hello, there!","Welcome to the world of POKeMON!","My name is OAK.","People affectionately refer to me","This world..."]
active_message_top = 0
message_top = messages_top[active_message_top]

messages_bottom = ["Glad to meet you!","","","as the POKeMON PROFESSOR.",""]
active_message_bottom = 0
message_bottom = messages_bottom[active_message_bottom]


image = pygame.image.load('ProfOak.jpg')
image = pygame.transform.scale(image, (width, height))

fade_box = pygame.image.load('Black.jpg').convert_alpha()
fade_box = pygame.transform.scale(fade_box, (width, height))


text_box = pygame.image.load('TextBox.png').convert_alpha()
text_box = pygame.transform.scale(text_box, (1024, 194))
poke_ball_notopen = pygame.image.load('PokeBall.png').convert_alpha()
poke_ball_notopen = pygame.transform.scale(poke_ball_notopen, (40, 40))

poke_ball_half = pygame.image.load('PokeBallHalf.png').convert_alpha()
poke_ball_half = pygame.transform.scale(poke_ball_half, (40, 40))

timer = pygame.time.Clock()

timer_event = pygame.event.custom_type()
fade_event = pygame.event.custom_type()







running = True


counter,counter2,counter3 = 0,0,0
done_top = False
done_bottom = False
speed = 3
fade2 = 255


def dropShadowText_Top(screen, text, size, x, y, c, s,  colour=(120, 120, 120), drop_colour=(214, 214, 206),  font=None ):

    dropshadow_offset = 2 + (size // 5)
    text_font = pygame.font.Font('PokemonFont.ttf', 20)



    text_bitmap = text_font.render(text[0:c//s], True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text[0:c//s], True, colour)
    screen.blit(text_bitmap, (x, y))

def dropShadowText_Bottom(screen, text, size, x, y, c, s,  colour=(120, 120, 120), drop_colour=(214, 214, 206),  font=None ):

    dropshadow_offset = 2 + (size // 15)
    text_font = pygame.font.Font('PokemonFont.ttf', 20)



    text_bitmap = text_font.render(text[0:c//s], True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text[0:c//s], True, colour)
    screen.blit(text_bitmap, (x, y))

def profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom):





    music.play()
    check1 = 0
    fade_num = 255
    pygame.time.set_timer(timer_event,2000)
    pygame.time.set_timer(fade_event,200)
    text_box.set_alpha(0)

    while True:

        screen.blit(image, (0, 0))
        screen.blit(text_box, (0, 450))
        screen.blit(fade_box, (0, 0))
        fade_box.set_alpha(fade_num)



        timer.tick(60)





        if check1 == 4 and done_top == True:
            screen.blit(poke_ball_notopen, (408, 272))
            pygame.time.delay(1000)
            screen.blit(poke_ball_half, (408, 272))

        for event in pygame.event.get():
            if check1 < 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                        active_message_top += 1
                        active_message_bottom += 1

                        check1+=1
                        done_top = False
                        done_bottom = False

                        message_top = messages_top[active_message_top]
                        message_bottom = messages_bottom[active_message_bottom]


                        counter = 0
                        counter2 = 0
            if event.type == timer_event:
                text_box.set_alpha(255)
            if event.type == fade_event:
                fade_num -= 50

            print(fade_box.get_alpha())



        if text_box.get_alpha() == 255:
            if counter < speed * len(message_top):
                counter += 1

            elif counter >= speed * len(message_top):
                done_top = True

            if done_top == True:
                if counter2 < speed * len(message_bottom):
                    counter2 += 1

                elif counter2 >= speed * len(message_bottom):
                    done_bottom = True

            dropShadowText_Top(screen,message_top, 10, 73, 478, counter, speed)
            dropShadowText_Bottom(screen,message_bottom, 10, 73, 538, counter2, speed)

        pygame.display.update()

def fade(x):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == fade_event:
                x-=1

        if x == 128:
            break



vid = Video("PokemonIntro.mp4")
vid.set_size((width, height))

def intro():
    while True:
        vid.draw(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()

                profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom)

def main():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.update()


intro()







