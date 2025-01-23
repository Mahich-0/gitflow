from pygame.sprite import Sprite

from ImageLoad import load_image
from Constants import *
from Char import character


class BazeAttack(Sprite):
    def __init__(self):
        super().__init__(spell_group)

        self.image_orig = load_image('Yamato.png')
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        # self.rect.x = character.rect.centerx - 120
        # self.rect.y = character.rect.centery
        self.rect.center = character.rect.center
        self.rot = 0
        self.rot_speed = 7
        self.last_update = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, -self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        # pass

    def damage(self):
        return 5


class Spell1(Sprite):
    def __init__(self):
        super().__init__(spell_group)

        self.image = load_image('spell1.png')

        self.rect = self.image.get_rect()
        self.rect.center = character.rect.center

    def update(self):
        pass

    def damage(self):
        return 5


class Spell2(Sprite):
    def __init__(self):
        super().__init__(spell_group)

        self.image_orig = load_image('spell2.png')
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        self.rect.center = character.rect.center
        self.rot = 0
        self.rot_speed = 5
        self.last_update = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def damage(self):
        return 0
