from pygame.sprite import Sprite

from Globals import *
from ImageLoad import load_image


class Character(Sprite):
    def __init__(self):
        super().__init__(player_group)
        self.image = load_image('Character.png')
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2

        self.change_x = 0
        self.change_y = 0
        self.game_running = False
        self.hp = 500  # hp по умолчанию

    def update(self, villains):
        for vil in villains:
            if pygame.sprite.collide_mask(self, vil):
                self.hp -= 1

        if self.hp <= 0:
            self.game_running = False
            self.hp = 500
            villains.clear()
            for sprt in villain_group:
                sprt.kill()
