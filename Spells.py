import math

from pygame.sprite import Sprite

from ImageLoad import load_image
from Globals import *
from Char import character


class BazeAttack(Sprite):
    def __init__(self):
        super().__init__(base_group)

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
        self.damage = 0

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


class Spell1(Sprite):
    def __init__(self):
        super().__init__(spell1_group)

        self.image = load_image('spell1.png')

        self.rect = self.image.get_rect()
        self.rect.center = character.rect.center
        self.damage = 100
        self.dx = False
        self.dy = False

    def update(self, villains):
        if self.dx is False and self.dy is False:
            distances = dict()
            for vil in villains:
                dx, dy = character.rect.x - vil.rect.x, character.rect.y - vil.rect.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                distances[distance] = (vil.rect.x, vil.rect.y)

            coords = distances[min(distances.keys())]
            distance = min(distances.keys())

            if distance != 0:
                self.dx = (self.rect.centerx - coords[0]) / distance
                self.dy = (self.rect.centery - coords[1]) / distance

            x1, y1 = coords[0] - self.rect.centerx, coords[1] - self.rect.centery
            x2, y2 = 0, 5

            cos_a = (x1 * x2 + y1 * y2) / (math.sqrt(x1 ** 2 + y1 ** 2) * math.sqrt(x2 ** 2 + y2 ** 2))
            rot = math.acos(cos_a) * (180 / math.pi)

            if x1 < 0:
                self.image = pygame.transform.rotate(self.image, -rot)
            else:
                self.image = pygame.transform.rotate(self.image, rot)

        self.rect.centerx -= self.dx * 10
        self.rect.centery -= self.dy * 10

        if self.rect.centery >= HEIGHT or self.rect.centerx >= WIDTH or \
                self.rect.centery <= 0 or self.rect.centerx <= 0:
            self.kill()

    def go_left(self):
        # Сами функции будут вызваны позже из основного цикла
        # self.change_x = player_speed
        self.rect.centerx += player_speed  # Двигаем игрока по Х

    def go_right(self):
        # то же самое, но вправо
        # self.change_x = -player_speed
        self.rect.centerx -= player_speed

    def go_up(self):
        # Сами функции будут вызваны позже из основного цикла
        # self.change_y = player_speed
        self.rect.centery += player_speed  # Двигаем игрока по y

    def go_down(self):
        # self.change_y = -player_speed
        self.rect.centery -= player_speed


class Spell2(Sprite):
    def __init__(self):
        super().__init__(spell2_group)

        self.image_orig = load_image('spell2.png')
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        self.rect.center = character.rect.center
        self.rot = 0
        self.rot_speed = 5
        self.last_update = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        self.damage = 25
        self.duration = 10

    def update(self, update):
        if update < self.duration:
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center
        else:
            self.kill()
