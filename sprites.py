import pygame, sys

class NameSelectSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, gender,w,h):
        super().__init__()
        self.sprites = []
        image1 = pygame.image.load("IntroImages/"+gender+"1.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load("IntroImages/"+gender + "2.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load("IntroImages/"+gender + "3.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites.append(image1)
        image1 = pygame.image.load("IntroImages/"+gender + "2.png")
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


class LetterSpaceSprite(NameSelectSprite):
    def __init__(self, pos_x, pos_y, gender,w,h):
        super().__init__(pos_x,pos_y,gender,w,h)
        self.sprites = []
        self.is_animating = False
        for x in range(1,5):
            image1 = pygame.image.load("IntroImages/"+gender + str(x)+".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)
        for x in range(3,1,-1):
            image1 = pygame.image.load("IntroImages/"+gender + str(x) + ".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)

    def animate(self):
        self.is_animating = True
    def animate_off(self, gender,w ,h):
        image1 = pygame.image.load("IntroImages/"+gender + "1.png")
        image1 = pygame.transform.scale(image1, (w, h))
        self.sprites = [image1]


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
            image1 = pygame.image.load("IntroImages/"+gender + str(x) + ".png")
            image1 = pygame.transform.scale(image1, (w, h))
            self.sprites.append(image1)

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, gender, s):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.sprites2 = []
        self.sprites3 = []
        self.sprites4 = []
        image1 = pygame.image.load("GameImages/" + gender + "Down"+"2.png")
        image1 = pygame.transform.scale_by(image1, (s))
        self.sprites.append(image1)
        for x in range(1, 4):
            image1 = pygame.image.load("GameImages/" + gender + "Down"+ str(x) + ".png")
            image1 = pygame.transform.scale_by(image1, (s))
            self.sprites.append(image1)
        image1 = pygame.image.load("GameImages/" + gender + "Up"+"2.png")
        image1 = pygame.transform.scale_by(image1, (s))
        self.sprites2.append(image1)
        for x in range(1, 4):
            image1 = pygame.image.load("GameImages/" + gender + "Up"+ str(x) + ".png")
            image1 = pygame.transform.scale_by(image1, (s))
            self.sprites2.append(image1)

l
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.09
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


