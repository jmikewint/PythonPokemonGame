import pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1024, 628))
test1 = pygame.image.load('ProfOak_Back.jpg')
test1 = pygame.transform.scale(test1, (1024, 628))
nemesis = pygame.image.load('Nemesis.png').convert_alpha()
nemesis = pygame.transform.scale(nemesis, (130, 325))
text_box = pygame.image.load('TextBox.png').convert_alpha()
text_box = pygame.transform.scale(text_box, (1024, 194))


timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 200)

nx = 450

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == timer_event:
            nx += 10

    screen.blit(test1, [0, 0])
    screen.blit(nemesis, [nx, 128])
    screen.blit(text_box, (0, 450))

    pygame.display.flip()



    clock.tick(20)