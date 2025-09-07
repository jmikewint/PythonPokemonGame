import pygame
from time import sleep

from Sprites import NameSelectSprite
from pyvidplayer import Video


pygame.init()
import requests
import time



width, height = 1024, 648
GREY = (99, 99, 99)
GREY_BACK= (214, 214, 206)


music = pygame.mixer.Sound("OakTheme.mp3")

font  = pygame.font.Font('PokemonFont.ttf', 20)

screen = pygame.display.set_mode((width, height))

messages_top = ["Hello, there!","Welcome to the world of POKeMON!","My name is OAK.","People affectionately refer to me","This world...","...is inhabited far and wide by","For some people, POKeMON are pets.","As for myself...","I study POKeMON as a profession.","But first, tell me a little about","Now tell me. Are you a  boy?","Let's begin with you name."]
active_message_top = 0
message_top = messages_top[active_message_top]

messages_bottom = ["Glad to meet you!","","","as the POKeMON PROFESSOR.","","creatures called POKeMON.","Others use them for battling.","","","yourself.","Or are you a girl?","What is it?"]
active_message_bottom = 0
message_bottom = messages_bottom[active_message_bottom]


image = pygame.image.load('ProfOak.jpg')
image = pygame.transform.scale(image, (width, height))
image2 = pygame.image.load('ProfOak_Back.jpg').convert_alpha()
image2 = pygame.transform.scale(image2, (width, height))
image3 = pygame.image.load('Oak_Platform.png').convert_alpha()
image3 = pygame.transform.scale(image3, (350, 75))

nidoran = pygame.image.load('NidoranIntro.png')
nidoran = pygame.transform.scale(nidoran, (120, 120))
boy = pygame.image.load('Boy.png').convert_alpha()
boy = pygame.transform.scale(boy, (130, 315))
girl = pygame.image.load('Girl.png').convert_alpha()
girl = pygame.transform.scale(girl, (130, 315))


fade_box = pygame.image.load('Black.jpg').convert_alpha()
fade_box = pygame.transform.scale(fade_box, (width, height))

flash_box = pygame.image.load('White.jpg').convert_alpha()
flash_box = pygame.transform.scale(flash_box, (width, height))


name_select = pygame.image.load('Name_Select.jpg').convert_alpha()
name_select = pygame.transform.scale(name_select, (width, height))


text_box = pygame.image.load('TextBox.png').convert_alpha()
text_box = pygame.transform.scale(text_box, (1024, 194))
gender_box = pygame.image.load('Gender_Select.png').convert_alpha()
gender_box = pygame.transform.scale(gender_box, (300, 164))
gender_arrow = pygame.image.load('Gender_Arrow.png').convert_alpha()
gender_arrow = pygame.transform.scale(gender_arrow, (20, 33))


poke_ball_notopen = pygame.image.load('PokeBall.png').convert_alpha()
poke_ball_notopen = pygame.transform.scale(poke_ball_notopen, (40, 40))

poke_ball_half = pygame.image.load('PokeBallHalf.png').convert_alpha()
poke_ball_half = pygame.transform.scale(poke_ball_half, (40, 40))

timer = pygame.time.Clock()

timer_event = pygame.event.custom_type()
fade_event = pygame.event.custom_type()
flash_event = pygame.event.custom_type()

fade_num = 255
faded = False
flash_num = 0
flashed = False




running = True


counter,counter2,counter3 = 0,0,0
done_top = False
done_bottom = False
speed = 10


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

def dropShadowText(screen, text, size, x, y, colour=(120, 120, 120), drop_colour=(214, 214, 206),  font=None ):

    dropshadow_offset = 2 + (size // 15)
    text_font = pygame.font.Font('PokemonFont.ttf', 20)



    text_bitmap = text_font.render(text, True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text, True, colour)
    screen.blit(text_bitmap, (x, y))

#
# def profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom):
#     global faded, fade_num, flashed, flash_num
#     check = 0
#     dialogue_index = 0
#     gender = [boy,girl]
#     index = 0
#
#     def fade():
#         global fade_num
#         global faded
#         pygame.time.delay(220)
#         fade_num-=51
#         nidoran.set_alpha(0)
#         if fade_num < -150:
#             pygame.time.delay(1500)
#             faded = True
#             return faded
#
#     def flash_in():
#         global flashed
#         global flash_num
#         pygame.time.delay(140)
#         flash_num+=51
#
#         if flash_num > 335:
#             flashed = True
#             return flashed
#
#     def flash_out():
#         global flashed
#         global flash_num
#         pygame.time.delay(140)
#         flash_num -= 51
#         if flash_num < -305:
#             flashed = False
#             return flashed
#
#     def test_fade(width, height):
#         testing_fade = pygame.Surface((width, height))
#         testing_fade.fill((0, 0, 0))
#         for alpha in range(0,255):
#             testing_fade.set_alpha(alpha)
#             screen.blit(testing_fade, (0, 0))
#             pygame.display.update()
#             pygame.time.delay(20)
#
#
#
#     #
#     #
#     # while check == 0:
#     #     for event in pygame.event.get():
#     #         if event.type == pygame.QUIT:
#     #             pygame.quit()
#     #         elif dialogue_index < 4 or 4 < dialogue_index < 9:
#     #             if event.type == pygame.KEYDOWN:
#     #                 if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
#     #                     active_message_top += 1
#     #                     active_message_bottom += 1
#     #
#     #                     dialogue_index+=1
#     #                     done_top = False
#     #                     done_bottom = False
#     #
#     #                     message_top = messages_top[active_message_top]
#     #                     message_bottom = messages_bottom[active_message_bottom]
#     #
#     #
#     #                     counter = 0
#     #                     counter2 = 0
#     #
#     #         elif dialogue_index == 9:
#     #             if event.type == pygame.KEYDOWN:
#     #                 if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
#     #                     check = 1
#     #
#     #                     active_message_top += 1
#     #                     active_message_bottom += 1
#     #
#     #                     dialogue_index += 1
#     #                     done_top = False
#     #                     done_bottom = False
#     #
#     #                     message_top = messages_top[active_message_top]
#     #                     message_bottom = messages_bottom[active_message_bottom]
#     #
#     #                     counter = 0
#     #                     counter2 = 0
#     #                     break
#     #
#     #     screen.blit(image, (0, 0))
#     #     screen.blit(nidoran, (350, 325))
#     #     screen.blit(flash_box, (0, 0))
#     #     flash_box.set_alpha(flash_num)
#     #     screen.blit(text_box, (0, 450))
#     #     text_box.set_alpha(0)
#     #     screen.blit(fade_box, (0, 0))
#     #     fade_box.set_alpha(fade_num)
#     #
#     #     print(dialogue_index)
#     #
#     #     if faded == False:
#     #         fade()
#     #     if faded == True:
#     #         text_box.set_alpha(255)
#     #         if counter < speed * len(message_top):
#     #             counter += 1
#     #         elif counter >= speed * len(message_top):
#     #             done_top = True
#     #         if done_top == True:
#     #             if counter2 < speed * len(message_bottom):
#     #                 counter2 += 1
#     #             elif counter2 >= speed * len(message_bottom):
#     #                 done_bottom = True
#     #
#     #         dropShadowText_Top(screen,message_top, 10, 73, 478, counter, speed)
#     #         dropShadowText_Bottom(screen,message_bottom, 10, 73, 538, counter2, speed)
#     #
#     #     if dialogue_index == 4 and done_top == True:
#     #         flash_in()
#     #         if flash_num >200 and 300 > flash_num:
#     #
#     #             active_message_top = 5
#     #             active_message_bottom = 5
#     #
#     #
#     #             done_top = False
#     #             done_bottom = False
#     #
#     #             message_top = messages_top[active_message_top]
#     #             message_bottom = messages_bottom[active_message_bottom]
#     #
#     #             counter = 0
#     #             counter2 = 0
#     #
#     #     if flashed == True:
#     #         dialogue_index = 5
#     #         nidoran.set_alpha(255)
#     #         flash_out()
#     #
#     #
#     #     pygame.display.update()
#
#     for x in range(255, -250, -5):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#
#         screen.blit(image2, (0, 0))
#         screen.blit(image, (0, 0))
#         pygame.time.delay(18)
#         image.set_alpha(x)
#         pygame.display.update()
#
#     pygame.time.wait(500)
#     gy = 320
#     gx = 700
#     while check == 0:
#
#         message_top = messages_top[10]
#         message_bottom = messages_bottom[10]
#
#         faded = True
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYDOWN:
#                 if gy != 380:
#                     if event.key == pygame.K_DOWN:
#                         gy += 60
#                     elif event.key == pygame.K_RETURN:
#                         check = 2
#                         index = 0
#                         active_message_top += 1
#                         active_message_bottom += 1
#
#                         dialogue_index += 1
#                         done_top = False
#                         done_bottom = False
#
#                         message_top = messages_top[active_message_top]
#                         message_bottom = messages_bottom[active_message_bottom]
#
#                         counter = 0
#                         counter2 = 0
#                         break
#                 elif gy != 320:
#                     if event.key == pygame.K_UP:
#                         gy -= 60
#                     elif event.key == pygame.K_RETURN:
#                         check = 2
#                         index = 1
#                         active_message_top += 1
#                         active_message_bottom += 1
#
#                         dialogue_index += 1
#                         done_top = False
#                         done_bottom = False
#
#                         message_top = messages_top[active_message_top]
#                         message_bottom = messages_bottom[active_message_bottom]
#
#                         counter = 0
#                         counter2 = 0
#                         break
#
#         screen.blit(image2, (0, 0))
#         screen.blit(text_box, (0, 450))
#         screen.blit(gender_box, (660, 285))
#         screen.blit(gender_arrow, (gx, gy))
#
#
#         dropShadowText(screen, "BOY", 10, 723, 305)
#         dropShadowText(screen, "GIRL", 10, 723, 365)
#
#
#         if faded == True:
#             if counter < speed * len(message_top):
#                 counter += 1
#             elif counter >= speed * len(message_top):
#                 done_top = True
#             if done_top == True:
#                 if counter2 < speed * len(message_bottom):
#                     counter2 += 1
#                 elif counter2 >= speed * len(message_bottom):
#                     done_bottom = True
#
#             dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
#             dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)
#
#         pygame.display.update()
#
#
#
#     for x in range(255, -250, -5):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#         screen.blit(image3, (330, 395))
#         screen.blit(gender[index], (450, 128))
#         screen.blit(image2, (0, 0))
#         pygame.time.delay(18)
#         image2.set_alpha(x)
#
#         pygame.display.update()
#
#     pygame.time.wait(100)
#
#     while check == 2:
#         message_top = messages_top[11]
#         message_bottom = messages_bottom[11]
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
#                     test_fade(1024,648)
#                     name_selecting()
#
#
#         screen.blit(image3, (330, 395))
#         screen.blit(gender[index], (450, 128))
#         screen.blit(text_box, (0, 450))
#
#
#         if faded == True:
#             if counter < speed * len(message_top):
#                 counter += 1
#             elif counter >= speed * len(message_top):
#                 done_top = True
#             if done_top == True:
#                 if counter2 < speed * len(message_bottom):
#                     counter2 += 1
#                 elif counter2 >= speed * len(message_bottom):
#                     done_bottom = True
#
#             dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
#             dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)
#
#         pygame.display.update()
#         # #music.play()
#         # pygame.time.set_timer(fade_event,3000)


def name_selecting():
    boy_select = NameSelectSprite(212, 145,"Boy")
    hover = NameSelectSprite(138, 327,"Hover")

    boy_select.size_upd(58,73)
    hover.size_upd(47,63)

    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(boy_select)
    moving_sprites.add(hover)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(name_select, (0, 0))
        moving_sprites.draw(screen)
        moving_sprites.update()
        pygame.display.update()






# vid = Video("PokemonIntro.mp4")
# vid.set_size((width, height))
#
# def intro():
#     while True:
#         vid.draw(screen,(0,0))
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 vid.close()
#                 profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom)



def main():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.update()


name_selecting()






