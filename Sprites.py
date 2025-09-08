import pygame, sys

class NameSelectSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, gender,w,h):
        super().__init__()
        self.sprites = []
        image1 = pygame.image.load(gender+"1.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load(gender + "2.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load(gender + "3.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load(gender + "2.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.007

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



    def move(self, pos_x, pos_y):
        self.rect.x += pos_x
        self.rect.y += pos_y

class LetterSpaceSprite(NameSelectSprite):
    def __init__(self, pos_x, pos_y, gender,w,h):
        super().__init__(pos_x,pos_y,gender,w,h)
        self.sprites = []
        self.is_animating = False
        for x in range(1,5):
            image1 = pygame.image.load(gender + str(x)+".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)
        for x in range(3,1,-1):
            image1 = pygame.image.load(gender + str(x) + ".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)

    def animate(self):
        self.is_animating = True
    def animate_off(self, gender,w ,h):
        image1 = pygame.image.load(gender + "1.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites = [image1]


    def check(self):
        print(self.sprites)
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.01
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


class NameSelectArrow(NameSelectSprite):
    def __init__(self, pos_x, pos_y, gender,w,h):
        super().__init__(pos_x,pos_y,gender,w,h)
        self.sprites = []
        for x in range(1, 5):
            image1 = pygame.image.load(gender + str(x) + ".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)


