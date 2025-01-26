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
        self.last_update = 0
        self.last_heal = 0
        self.hp = 500
        self.kills_count = 0

    def update(self, villains):
        now = pygame.time.get_ticks()
        for vil in villains:
            if pygame.sprite.collide_mask(self, vil):
                if now - self.last_update > FPS * 10:
                    self.last_update = now
                    self.hp -= 25

        if now - self.last_update > FPS * 20:
            if self.hp < 500:
                if now - self.last_heal > FPS * 10:
                    self.last_heal = now
                    self.hp += 5

        if self.hp <= 0:
            self.game_running = False
            self.hp = 500
            villains.clear()
            for sprt in villain_group:
                sprt.kill()
