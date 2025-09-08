import pygame
from time import sleep

from Sprites import NameSelectSprite, LetterSpaceSprite, NameSelectArrow
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

messages_top = ["Hello, there!","Welcome to the world of POKeMON!","My name is OAK.","People affectionately refer to me","This world...","...is inhabited far and wide by","For some people, POKeMON are pets.","As for myself...","I study POKeMON as a profession.","But first, tell me a little about","Now tell me. Are you a  boy?","Let's begin with you name.","Right..."]
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

word = ""
gy = 320
gx = 700

running = True


counter,counter2,counter3 = 0,0,0
done_top = False
done_bottom = False
speed = 5



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

    dropshadow_offset = 2 + (size //9)
    text_font = pygame.font.Font('PokemonFont.ttf', 20)



    text_bitmap = text_font.render(text, True, drop_colour)
    screen.blit(text_bitmap, (x + dropshadow_offset, y + dropshadow_offset))

    text_bitmap = text_font.render(text, True, colour)
    screen.blit(text_bitmap, (x, y))


def test_fade(width, height):
    testing_fade = pygame.Surface((width, height))
    testing_fade.fill((0, 0, 0))
    for alpha in range(0,255):
        testing_fade.set_alpha(alpha)
        screen.blit(testing_fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(20)

def profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom):
    global faded, fade_num, flashed, flash_num, gx,gy
    check = 3
    dialogue_index = 0
    gender = [boy,girl]
    index = 0

    def fade():
        global fade_num
        global faded
        pygame.time.delay(220)
        fade_num-=51
        nidoran.set_alpha(0)
        if fade_num < -150:
            pygame.time.delay(1500)
            faded = True
            return faded

    def flash_in():
        global flashed
        global flash_num
        pygame.time.delay(140)
        flash_num+=51

        if flash_num > 335:
            flashed = True
            return flashed

    def flash_out():
        global flashed
        global flash_num
        pygame.time.delay(140)
        flash_num -= 51
        if flash_num < -305:
            flashed = False
            return flashed







    while check == 0:
        #music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif dialogue_index < 4 or 4 < dialogue_index < 9:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                        active_message_top += 1
                        active_message_bottom += 1

                        dialogue_index+=1
                        done_top = False
                        done_bottom = False

                        message_top = messages_top[active_message_top]
                        message_bottom = messages_bottom[active_message_bottom]


                        counter = 0
                        counter2 = 0

            elif dialogue_index == 9:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                        check = 1

                        active_message_top += 1
                        active_message_bottom += 1

                        dialogue_index += 1
                        done_top = False
                        done_bottom = False

                        message_top = messages_top[active_message_top]
                        message_bottom = messages_bottom[active_message_bottom]

                        counter = 0
                        counter2 = 0
                        break

        screen.blit(image, (0, 0))
        screen.blit(nidoran, (350, 325))
        screen.blit(flash_box, (0, 0))
        flash_box.set_alpha(flash_num)
        screen.blit(text_box, (0, 450))
        text_box.set_alpha(0)
        screen.blit(fade_box, (0, 0))
        fade_box.set_alpha(fade_num)


        if faded == False:
            fade()
        if faded == True:
            text_box.set_alpha(255)
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

        if dialogue_index == 4 and done_top == True:
            flash_in()
            if flash_num >200 and 300 > flash_num:

                active_message_top = 5
                active_message_bottom = 5


                done_top = False
                done_bottom = False

                message_top = messages_top[active_message_top]
                message_bottom = messages_bottom[active_message_bottom]

                counter = 0
                counter2 = 0

        if flashed == True:
            dialogue_index = 5
            nidoran.set_alpha(255)
            flash_out()


        pygame.display.update()

    if check == 1:
        for x in range(255, -250, -5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            screen.blit(image2, (0, 0))
            screen.blit(image, (0, 0))
            pygame.time.delay(18)
            image.set_alpha(x)
            pygame.display.update()

        pygame.time.wait(500)


    while check == 1:


        faded = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if gy != 380:
                    if event.key == pygame.K_DOWN:
                        gy += 60
                    elif event.key == pygame.K_RETURN:
                        check = 2
                        index = 0
                        active_message_top += 1
                        active_message_bottom += 1

                        dialogue_index += 1
                        done_top = False
                        done_bottom = False

                        message_top = messages_top[active_message_top]
                        message_bottom = messages_bottom[active_message_bottom]

                        counter = 0
                        counter2 = 0
                        break
                elif gy != 320:
                    if event.key == pygame.K_UP:
                        gy -= 60
                    elif event.key == pygame.K_RETURN:
                        check = 2
                        index = 1
                        active_message_top += 1
                        active_message_bottom += 1

                        dialogue_index += 1
                        done_top = False
                        done_bottom = False

                        message_top = messages_top[active_message_top]
                        message_bottom = messages_bottom[active_message_bottom]

                        counter = 0
                        counter2 = 0
                        break

        screen.blit(image2, (0, 0))
        screen.blit(text_box, (0, 450))
        screen.blit(gender_box, (660, 285))
        screen.blit(gender_arrow, (gx, gy))


        dropShadowText(screen, "BOY", 10, 723, 305)
        dropShadowText(screen, "GIRL", 10, 723, 365)


        if faded == True:
            if counter < speed * len(message_top):
                counter += 1
            elif counter >= speed * len(message_top):
                done_top = True
            if done_top == True:
                if counter2 < speed * len(message_bottom):
                    counter2 += 1
                elif counter2 >= speed * len(message_bottom):
                    done_bottom = True

            dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
            dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)

        pygame.display.update()


    if check == 2:
        for x in range(255, -250, -5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            screen.blit(image3, (330, 395))
            screen.blit(gender[index], (450, 128))
            screen.blit(image2, (0, 0))
            pygame.time.delay(18)
            image2.set_alpha(x)

            pygame.display.update()

    pygame.time.wait(100)

    while check == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                    check = 3
                    active_message_top += 1
                    active_message_bottom += 1

                    dialogue_index += 1
                    done_top = False
                    done_bottom = False

                    message_top = messages_top[active_message_top]
                    message_bottom = messages_bottom[active_message_bottom]

                    counter = 0
                    counter2 = 0
                    test_fade(1024,648)
                    name_selecting()


        screen.blit(image3, (330, 395))
        screen.blit(gender[index], (450, 128))
        screen.blit(text_box, (0, 450))


        if faded == True:
            if counter < speed * len(message_top):
                counter += 1
            elif counter >= speed * len(message_top):
                done_top = True
            if done_top == True:
                if counter2 < speed * len(message_bottom):
                    counter2 += 1
                elif counter2 >= speed * len(message_bottom):
                    done_bottom = True

            dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
            dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)

        pygame.display.update()
       # pygame.time.set_timer(fade_event,3000)

    testing = "".join(word.split())
    messages_bottom.append("So your name is "+testing+".")
    gx = 80
    gy = 80


    # while check == 3:
    #     message_tops = messages_top[12]
    #     message_bottom = messages_bottom[12]
    #     dialogue_index = 12
    #     faded = True
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #         if event.type == pygame.KEYDOWN:
    #             if gy != 140:
    #                 if event.key == pygame.K_DOWN:
    #                     gy += 60
    #                 elif event.key == pygame.K_RETURN:
    #                     check = 4
    #                     index = 0
    #                     active_message_top += 1
    #                     active_message_bottom += 1
    #
    #                     dialogue_index += 1
    #                     done_top = False
    #                     done_bottom = False
    #
    #                     message_top = messages_top[active_message_top]
    #                     message_bottom = messages_bottom[active_message_bottom]
    #
    #                     counter = 0
    #                     counter2 = 0
    #                     break
    #             elif gy != 80:
    #                 if event.key == pygame.K_UP:
    #                     gy -= 60
    #                 elif event.key == pygame.K_RETURN:
    #                     check = 2
    #                     index = 1
    #                     active_message_top += 1
    #                     active_message_bottom += 1
    #
    #                     dialogue_index += 1
    #                     done_top = False
    #                     done_bottom = False
    #
    #                     message_top = messages_top[active_message_top]
    #                     message_bottom = messages_bottom[active_message_bottom]
    #
    #                     counter = 0
    #                     counter2 = 0
    #                     break
    #     screen.blit(image2,(0, 0))
    #     screen.blit(image3, (580, 395))
    #     screen.blit(gender[index], (700, 128))
    #     screen.blit(text_box, (0, 450))
    #
    #     if faded == True:
    #         if counter < speed * len(message_top):
    #             counter += 1
    #         elif counter >= speed * len(message_top):
    #             done_top = True
    #         if done_top == True:
    #             if counter2 < speed * len(message_bottom):
    #                 counter2 += 1
    #             elif counter2 >= speed * len(message_bottom):
    #                 done_bottom = True
    #
    #         dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
    #         dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)
    #
    #     if dialogue_index == 12 and done_top == True and done_bottom == True:
    #         screen.blit(gender_box, (40, 45))
    #         screen.blit(gender_arrow, (gx, gy))
    #         dropShadowText(screen, "Yes", 10, 104, 65)
    #         dropShadowText(screen, "No", 10, 108, 125)
    #
    #
    #     pygame.display.update()

    for x in range(255, -250, -5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(image2, (0, 0))
        screen.blit(image3, (580, 395))
        screen.blit(gender[index], (700, 128))
        pygame.time.delay(18)
        image3.set_alpha(x)
        gender[index].set_alpha(x)
        pygame.display.update()


def name_selecting():
    global word
    boy_select = NameSelectSprite(212, 145,"Boy",58,73)
    hover = NameSelectSprite(138, 327,"Hover",47,63)
    name_arrow = NameSelectArrow(368, 211,"Name_Arrow",100,33)
    spaces = []
    space_x = 420



    for x in range(7):
        letter_space = LetterSpaceSprite(space_x, 241, "Letter_Space",30,25)
        #letter_space.size_upd(30, 25)
        spaces.append(letter_space)
        space_x += 38

    #
    # boy_select.size_upd(58,73)
    # hover.size_upd(47,63)
    # name_arrow.size_upd(120,40)



    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(boy_select)
    moving_sprites.add(hover)
    moving_sprites.add(name_arrow)
    moving_sprites.add(spaces)



    letter_index = 1
    active_letter = 0
    letter = 1
    side_x = False

    file = open("Alphabet.txt")
    alphabet = {}
    word= ""

    set = []
    z = 1
    y = 1

    for x in range(1, 27, 1):
        new_letter = {x: file.readline().strip()}
        alphabet.update(new_letter)




    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_RETURN:
                        word += alphabet.get(letter) + " "
                        active_letter = letter_index
                        letter_index += 1
                    elif event.key == pygame.K_SPACE:
                        test_fade(1024,648)
                        profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom,active_message_top, active_message_bottom)
                    if y > 2:
                        side_x = True
                    else:
                        side_x = False
                    if event.key == pygame.K_RIGHT:
                        if side_x == False:
                            if z == 6:
                                raise ValueError
                        if side_x == True:
                            if z == 7:
                                raise ValueError
                        if z == 3:
                            z += 1
                            letter += 1
                            hover.move(137, 0)
                        else:
                            z += 1
                            letter += 1
                            hover.move(51, 0)
                    if event.key == pygame.K_LEFT:
                        if z == 1:
                            raise ValueError
                        if z == 4:
                            z -= 1
                            letter -= 1
                            hover.move(-137, 0)
                        elif z != 4:
                            z -= 1
                            letter -= 1
                            hover.move(-51, 0)
                    if event.key == pygame.K_DOWN:
                        if y == 4:
                            raise ValueError
                        if y < 3:
                            letter+=6
                        else:
                            letter+=7
                        y+=1
                        hover.move(0, 64)
                    if event.key == pygame.K_UP:
                        if y == 1:
                            raise ValueError
                        if z == 7 and y == 3:
                            raise ValueError
                        if y < 4:
                            letter -= 6
                        else:
                            letter -= 7
                        y -= 1
                        hover.move(0, -64)
                except ValueError:
                    print("no")


        screen.blit(name_select, (0, 0))
        moving_sprites.draw(screen)
        moving_sprites.update()
        match letter_index:
            case 1:
                spaces[0].animate()
            case 2:
                spaces[0].animate_off("Letter_Space",30,25)
                spaces[1].animate()
                #dropShadowText(screen, alphabet.get(active_letter), 10, 424, 190)
            case 3:
                spaces[1].animate_off("Letter_Space",30,25)
                spaces[2].animate()
            case 4:
                spaces[2].animate_off("Letter_Space",30,25)
                spaces[3].animate()
            case 5:
                spaces[3].animate_off("Letter_Space",30,25)
                spaces[4].animate()
            case 6:
                spaces[4].animate_off("Letter_Space",30,25)
                spaces[5].animate()
            case 7:
                spaces[5].animate_off("Letter_Space",30,25)
                spaces[6].animate()

        dropShadowText(screen, word, 10, 424, 190)

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
#


def main():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


        pygame.display.update()


profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom)




