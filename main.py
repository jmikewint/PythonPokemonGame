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

messages_top = ["Hello, there!","Welcome to the world of POKeMON!","My name is OAK.","People affectionately refer to me","This world...","...is inhabited far and wide by","For some people, POKeMON are pets.","As for myself...","I study POKeMON as a profession.","But first, tell me a little about","Now tell me. Are you a  boy?","Let's begin with your name.","Right...","This is my grandson.","He's been your rival since you both","...Erm, what was his name now?"]
active_message_top = 0
message_top = messages_top[active_message_top]

messages_bottom = ["Glad to meet you!","","","as the POKeMON PROFESSOR.","","creatures called POKeMON.","Others use them for battling.","","","yourself.","Or are you a girl?","What is it?","","","were babies.",""]
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
nemesis = pygame.image.load('Nemesis.png').convert_alpha()
nemesis = pygame.transform.scale(nemesis, (130, 325))

fade_box = pygame.image.load('Black.jpg').convert_alpha()
fade_box = pygame.transform.scale(fade_box, (width, height))

flash_box = pygame.image.load('White.jpg').convert_alpha()
flash_box = pygame.transform.scale(flash_box, (width, height))


name_select = pygame.image.load('Name_Select.jpg').convert_alpha()
name_select = pygame.transform.scale(name_select, (width, height))


text_box = pygame.image.load('TextBox.png').convert_alpha()
text_box = pygame.transform.scale(text_box, (1024, 194))
gender_box = pygame.image.load('Gender_Select.png').convert_alpha()
gender_box = pygame.transform.scale(gender_box, (300, 163))
gender_box2 = pygame.image.load('Gender_Select.png').convert_alpha()
gender_box2 = pygame.transform.scale(gender_box2, (500, 380))
gender_arrow = pygame.image.load('Gender_Arrow.png').convert_alpha()
gender_arrow = pygame.transform.scale(gender_arrow, (20, 33))


poke_ball_notopen = pygame.image.load('PokeBall.png').convert_alpha()
poke_ball_notopen = pygame.transform.scale(poke_ball_notopen, (40, 40))

poke_ball_half = pygame.image.load('PokeBallHalf.png').convert_alpha()
poke_ball_half = pygame.transform.scale(poke_ball_half, (40, 40))

timer = pygame.time.Clock()

timer_event = pygame.event.custom_type()

gy = 320
gx = 700

running = True


counter,counter2,counter3, dialogue_index, index,check = 0,0,0,0,0,0
done_top = False
done_bottom = False
speed = 1



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
    for alpha in range(0,20):
        testing_fade.set_alpha(alpha)
        screen.blit(testing_fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def text_reset(act_top, act_bottom,dial,done_top,done_bottom,mes_top,mes_bottom,mess_top, mess_bottom,count,count2):
    act_top += 1
    act_bottom += 1
    dial += 1
    done_top = False
    done_bottom = False
    mes_top = mess_top[act_top]
    mes_bottom = mess_bottom[act_bottom]
    counter = 0
    counter2 = 0

def profoak_intro(counter, counter2, message_top, message_bottom, done_top, done_bottom, active_message_top, active_message_bottom):
    global gx,gy,dialogue_index,index,check
    gender = [boy,girl]

    boy_select = NameSelectSprite(212, 145,"Boy",58,73)
    hover = NameSelectSprite(138, 327,"Hover",47,63)
    name_arrow = NameSelectArrow(368, 211,"Name_Arrow",100,33)
    spaces = []
    space_x = 420
    word = ""

    for x in range(7):
        letter_space = LetterSpaceSprite(space_x, 241, "Letter_Space", 30, 25)
        spaces.append(letter_space)
        space_x += 38

    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(boy_select)
    moving_sprites.add(hover)
    moving_sprites.add(name_arrow)
    moving_sprites.add(spaces)

    letter_index = 1
    letter = 1

    file = open("Alphabet.txt")
    alphabet = {}



    for x in range(1, 27, 1):
        new_letter = {x: file.readline().strip()}
        alphabet.update(new_letter)

    z = 1
    y = 1
    while True:
        if check == 0:
            pygame.time.set_timer(timer_event, 50)
            for x in range(255, -300, -50):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                screen.blit(image, (0, 0))
                screen.blit(fade_box, (0, 0))
                pygame.time.delay(158)
                fade_box.set_alpha(x)
                pygame.display.update()
            pygame.time.delay(150)
            while check == 0:
                music.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif dialogue_index < 4 or 4 < dialogue_index < 9:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                active_message_top += 1
                                active_message_bottom += 1
                                dialogue_index += 1
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
                # screen.blit(nidoran, (350, 325))
                screen.blit(text_box, (0, 450))


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

                if dialogue_index == 4 and done_top == True:
                    x = 255
                    while x > -200:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == timer_event:
                                x -= 40

                        screen.blit(flash_box, (0, 0))
                        screen.blit(image, (0, 0))
                        screen.blit(text_box, (0, 450))
                        image.set_alpha(x)

                        if x == 55:
                            active_message_top += 1
                            active_message_bottom += 1
                            done_top = False
                            done_bottom = False
                            message_top = messages_top[active_message_top]
                            message_bottom = messages_bottom[active_message_bottom]
                            counter = 0
                            counter2 = 0
                            x -= 1

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
                    x = 255
                    image.set_alpha(255)
                    while x > -200:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == timer_event:
                                x -= 40
                        screen.blit(image, (0, 0))
                        screen.blit(flash_box, (0, 0))
                        screen.blit(text_box, (0, 450))
                        flash_box.set_alpha(x)

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
                    dialogue_index += 1
                pygame.display.update()

        elif check == 1:
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
                print(word)
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

        elif check == 2:
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

                            message_bottom = messages_bottom[active_message_bottom]
                            message_top = messages_top[active_message_top]

                            counter = 0
                            counter2 = 0
                            test_fade(1024, 648)
                            break

                screen.blit(image3, (330, 395))
                screen.blit(gender[index], (450, 128))
                screen.blit(text_box, (0, 450))

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

        elif check == 3:
            while check == 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        try:
                            if event.key == pygame.K_RETURN and check == 3:
                                word += alphabet.get(letter) + " "
                                letter_index += 1
                            elif event.key == pygame.K_SPACE:
                                test_fade(1024, 648)
                                check = 4
                                break
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
                                    letter += 6
                                else:
                                    letter += 7
                                y += 1
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
                        spaces[0].animate_off("Letter_Space", 30, 25)
                        spaces[1].animate()
                    case 3:
                        spaces[1].animate_off("Letter_Space", 30, 25)
                        spaces[2].animate()
                    case 4:
                        spaces[2].animate_off("Letter_Space", 30, 25)
                        spaces[3].animate()
                    case 5:
                        spaces[3].animate_off("Letter_Space", 30, 25)
                        spaces[4].animate()
                    case 6:
                        spaces[4].animate_off("Letter_Space", 30, 25)
                        spaces[5].animate()
                    case 7:
                        spaces[5].animate_off("Letter_Space", 30, 25)
                        spaces[6].animate()

                dropShadowText(screen, word, 10, 424, 190)

                pygame.display.update()

        elif check == 4:
            testing = "".join(word.split())
            messages_bottom[12]= "So your name is "+testing+"."
            message_bottom = messages_bottom[active_message_bottom]
            fade_box.set_alpha(255)
            image2.set_alpha(255)
            image3.set_alpha(255)
            gx = 80
            gy = 80

            for x in range(255, -250, -5):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                screen.blit(image2, (0, 0))
                screen.blit(image3, (580, 395))
                screen.blit(gender[index], (700, 128))
                screen.blit(fade_box, (0, 0))
                pygame.time.delay(18)
                fade_box.set_alpha(x)
                pygame.display.update()



            while check == 4:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if gy != 140:
                            if event.key == pygame.K_DOWN:
                                gy += 60
                            elif event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                check = 5
                                active_message_top += 1
                                active_message_bottom += 1
                                dialogue_index += 1
                                done_top = False
                                done_bottom = False
                                message_top = messages_top[active_message_top]
                                message_bottom = messages_bottom[active_message_bottom]
                                counter = 0
                                counter2 = 0
                        elif gy != 80:
                            if event.key == pygame.K_UP:
                                gy -= 60
                            elif event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                check = 5
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
                screen.blit(image3, (580, 395))
                screen.blit(gender[index], (700, 128))
                screen.blit(text_box, (0, 450))

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

                if dialogue_index == 12 and done_top == True and done_bottom == True:
                    screen.blit(gender_box, (40, 45))
                    screen.blit(gender_arrow, (gx, gy))
                    dropShadowText(screen, "Yes", 10, 104, 65)
                    dropShadowText(screen, "No", 10, 108, 125)


                pygame.display.update()

        elif check == 5:
            gender_box.set_alpha(0)

            pygame.time.set_timer(timer_event, 10)
            nx = 450
            fx = 330
            gy = 100
            nemesis_name = 0


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

            pygame.time.wait(100)

            for x in range(255, -250, -5):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                screen.blit(image3, (330, 395))
                screen.blit(nemesis, (450, 128))
                screen.blit(image2, (0, 0))
                image3.set_alpha(255)
                pygame.time.delay(18)
                image2.set_alpha(x)
                pygame.display.update()
            pygame.time.delay(100)

            while check == 5:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if dialogue_index < 15 or dialogue_index > 16:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                if dialogue_index == 17:
                                    check = 6
                                    break
                                active_message_top += 1
                                active_message_bottom += 1
                                dialogue_index += 1
                                done_top = False
                                done_bottom = False
                                message_top = messages_top[active_message_top]
                                message_bottom = messages_bottom[active_message_bottom]
                                counter = 0
                                counter2 = 0

                    if dialogue_index == 15:
                        if nx < 700:
                            if event.type == timer_event:
                                nx+=5
                                fx+=5
                        if nx == 700:
                            if event.type == pygame.KEYDOWN:
                                if gy != 320:
                                    if event.key == pygame.K_DOWN:
                                        gy+=55
                                if gy != 100:
                                    if event.key == pygame.K_UP:
                                        gy-=55
                                if event.key == pygame.K_RETURN:
                                    match gy:
                                        case 100:
                                            print("poo")
                                        case 155:
                                            messages_top.append("...Er, was it GREEN?")
                                            messages_bottom.append("")
                                            active_message_top += 1
                                            active_message_bottom += 1
                                            dialogue_index += 1
                                            done_top = False
                                            done_bottom = False
                                            message_top = messages_top[active_message_top]
                                            message_bottom = messages_bottom[active_message_bottom]
                                            counter = 0
                                            counter2 = 0
                                            gy = 80
                                            nemesis_name = 1
                                        case 210:
                                            messages_top.append("...Er, was it GARY?")
                                            messages_bottom.append("")
                                            active_message_top += 1
                                            active_message_bottom += 1
                                            dialogue_index += 1
                                            done_top = False
                                            done_bottom = False
                                            message_top = messages_top[active_message_top]
                                            message_bottom = messages_bottom[active_message_bottom]
                                            counter = 0
                                            counter2 = 0
                                            nemesis_name = 2
                                        case 265:
                                            messages_top.append("...Er, was it KAZ?")
                                            messages_bottom.append("")
                                            active_message_top += 1
                                            active_message_bottom += 1
                                            dialogue_index += 1
                                            done_top = False
                                            done_bottom = False
                                            message_top = messages_top[active_message_top]
                                            message_bottom = messages_bottom[active_message_bottom]
                                            counter = 0
                                            counter2 = 0
                                            nemesis_name = 3
                                        case 320:
                                            messages_top.append("...Er, was it TORU?")
                                            messages_bottom.append("")
                                            active_message_top += 1
                                            active_message_bottom += 1
                                            dialogue_index += 1
                                            done_top = False
                                            done_bottom = False
                                            message_top = messages_top[active_message_top]
                                            message_bottom = messages_bottom[active_message_bottom]
                                            counter = 0
                                            counter2 = 0
                                            nemesis_name = 4
                                    nx+=1
                    if dialogue_index == 16:
                        if event.type == pygame.KEYDOWN:
                            if gy != 140:
                                if event.key == pygame.K_DOWN:
                                    gy += 60
                                elif event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                    match nemesis_name:
                                        case 0:
                                            print("poo")
                                        case 1:
                                            messages_top.append("That's right! I remember now!")
                                            messages_bottom.append("His name is GREEN!")
                                            messages_top.append(word+"!")
                                            messages_bottom.append("")
                                        case 2:
                                            messages_top.append("That's right! I remember now!")
                                            messages_bottom.append("His name is GARY!")
                                            messages_top.append(word + "!")
                                            messages_bottom.append("")
                                        case 3:
                                            messages_top.append("That's right! I remember now!")
                                            messages_bottom.append("His name is KAZ!")
                                            messages_top.append(word + "!")
                                            messages_bottom.append("")
                                        case 4:
                                            messages_top.append("That's right! I remember now!")
                                            messages_bottom.append("His name is TORU!")
                                            messages_top.append(word + "!")
                                            messages_bottom.append("")

                                    active_message_top += 1
                                    active_message_bottom += 1
                                    dialogue_index += 1
                                    done_top = False
                                    done_bottom = False
                                    message_top = messages_top[active_message_top]
                                    message_bottom = messages_bottom[active_message_bottom]
                                    counter = 0
                                    counter2 = 0
                            elif gy != 80:
                                if event.key == pygame.K_UP:
                                    gy -= 60
                                elif event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                                    active_message_top += 1
                                    active_message_bottom += 1
                                    dialogue_index += 1
                                    done_top = False
                                    done_bottom = False
                                    message_top = messages_top[active_message_top]
                                    message_bottom = messages_bottom[active_message_bottom]
                                    counter = 0
                                    counter2 = 0

                if counter < speed * len(message_top):
                    counter += 1
                elif counter >= speed * len(message_top):
                    done_top = True
                if done_top == True:
                    if counter2 < speed * len(message_bottom):
                        counter2 += 1
                    elif counter2 >= speed * len(message_bottom):
                        done_bottom = True

                screen.blit(image2, [0, 0])
                image2.set_alpha(255)
                screen.blit(image3, [fx, 395])
                screen.blit(nemesis, [nx, 128])
                screen.blit(text_box, (0, 450))



                if nx == 700:
                    screen.blit(gender_box2, (40, 40))
                    screen.blit(gender_arrow, (100, gy))
                    dropShadowText(screen, "NEW NAME", 10, 130, 85)
                    dropShadowText(screen, "GREEN", 10, 130, 140)
                    dropShadowText(screen, "GARY", 10, 130, 195)
                    dropShadowText(screen, "KAZ", 10, 130, 250)
                    dropShadowText(screen, "TORU", 10, 130, 305)

                if dialogue_index == 16 and done_top == True:
                    gender_box.set_alpha(255)
                    screen.blit(gender_box, (40, 45))
                    screen.blit(gender_arrow, (gx, gy))
                    dropShadowText(screen, "Yes", 10, 104, 65)
                    dropShadowText(screen, "No", 10, 108, 125)




                dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
                dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)

                pygame.display.flip()

        elif check == 6:
            for x in range(255, -250, -5):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                image2.set_alpha(255)
                screen.blit(image2, [0, 0])
                screen.blit(image3, [580, 395])
                screen.blit(nemesis, [701, 128])
                pygame.time.delay(18)
                image3.set_alpha(x)
                nemesis.set_alpha(x)
                pygame.display.update()
            pygame.time.delay(300)
            for x in range(255, -250, -5):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                image3.set_alpha(255)
                gender[index].set_alpha(255)
                screen.blit(image3, (330, 395))
                screen.blit(gender[index], (450, 128))
                screen.blit(image2, (0, 0))
                pygame.time.delay(18)
                image2.set_alpha(x)
                pygame.display.update()
            pygame.time.wait(200)

            active_message_top += 1
            active_message_bottom += 1
            dialogue_index += 1
            done_top = False
            done_bottom = False
            message_top = messages_top[active_message_top]
            message_bottom = messages_bottom[active_message_bottom]
            counter = 0
            counter2 = 0

            messages_top.append("Your very own POKeMON legend is")
            messages_bottom.append("about to unfold!")
            messages_top.append("A world of dreams and adventures")
            messages_bottom.append("with POKeMON awaits! Let's go!")

            while check == 6:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and done_top and done_bottom and active_message_top < len(messages_top) and active_message_bottom < len(messages_bottom):
                            active_message_top += 1
                            active_message_bottom += 1

                            dialogue_index += 1
                            done_top = False
                            done_bottom = False

                            message_bottom = messages_bottom[active_message_bottom]
                            message_top = messages_top[active_message_top]

                            counter = 0
                            counter2 = 0

                if counter < speed * len(message_top):
                    counter += 1
                elif counter >= speed * len(message_top):
                    done_top = True
                if done_top == True:
                    if counter2 < speed * len(message_bottom):
                        counter2 += 1
                    elif counter2 >= speed * len(message_bottom):
                        done_bottom = True

                image2.set_alpha(255)
                screen.blit(image2, [0, 0])
                screen.blit(image3, (330, 395))
                screen.blit(gender[index], (450, 128))
                screen.blit(text_box, (0, 450))


                dropShadowText_Top(screen, message_top, 10, 73, 478, counter, speed)
                dropShadowText_Bottom(screen, message_bottom, 10, 73, 538, counter2, speed)

                pygame.display.update()







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




intro()

