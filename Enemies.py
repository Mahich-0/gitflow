import random
import math

from pygame.sprite import Sprite

from Globals import *
from ImageLoad import load_image
from Char import character


class Villain(Sprite):
    def __init__(self):
        super().__init__(villain_group)
        self.image = load_image('Enemy.png')

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-263, WIDTH + 263)
        self.rect.y = random.randrange(-263, HEIGHT + 263)
        while -0 <= self.rect.x <= WIDTH and -0 <= self.rect.y <= HEIGHT:
            self.rect.x = random.randrange(-263, WIDTH + 263)
            self.rect.y = random.randrange(-263, HEIGHT + 263)
        self.hp = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3

    def update(self, base, spell1, spell2):
        if self.hp == 0:
            self.kill()
        else:
            dx, dy = character.rect.x - self.rect.x, character.rect.y - self.rect.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Normalize the direction vector
            if distance != 0:
                dx /= distance
                dy /= distance

            # Move the enemy
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            if pygame.sprite.collide_mask(self, base):
                self.hp -= base.damage
            if spell1:
                if pygame.sprite.collide_mask(self, spell1):
                    self.hp -= spell1.damage
            if spell2:
                if pygame.sprite.collide_mask(self, spell2):
                    self.hp -= spell2.damage

    def go_left(self):
        # Сами функции будут вызваны позже из основного цикла
        # self.change_x = player_speed
        self.rect.x += player_speed  # Двигаем игрока по Х

    def go_right(self):
        # то же самое, но вправо
        # self.change_x = -player_speed
        self.rect.x -= player_speed

    def go_up(self):
        # Сами функции будут вызваны позже из основного цикла
        # self.change_y = player_speed
        self.rect.y += player_speed  # Двигаем игрока по y

    def go_down(self):
        # self.change_y = -player_speed
        self.rect.y -= player_speed
