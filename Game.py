import pygame

from sprites import PlayerSprite

pygame.init()

clock = pygame.time.Clock()




timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 200)
width, height = 1024, 648


screen = pygame.display.set_mode((width, height))


image = pygame.image.load('GameImages/Testing.png')
image = pygame.transform.scale_by(image, 5)

image_rect = image.get_rect()

screen_rect = screen.get_rect()
image_rect.center = screen_rect.center

boy_select = PlayerSprite(212, 145, "BoyDown", 5)
moving_sprites = pygame.sprite.Group()
moving_sprites.add(boy_select)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        image_rect.y -= 5
        boy_select.animate()
    if keys[pygame.K_DOWN]:
        image_rect.y += 5
    if keys[pygame.K_LEFT]:
        image_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        image_rect.x += 5

    screen.fill((0,0,0))
    screen.blit(image, image_rect)
    moving_sprites.draw(screen)
    moving_sprites.update()

    pygame.display.update()



