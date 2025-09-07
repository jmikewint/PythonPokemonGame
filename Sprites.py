import pygame, sys

class NameSelectSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, gender):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(gender+"1.png"))
        self.sprites.append(pygame.image.load(gender+"2.png"))
        self.sprites.append(pygame.image.load(gender+"3.png"))
        self.sprites.append(pygame.image.load(gender+"2.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (500,500))
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.005

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def size_upd(self, w,h):
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (w, h))