import math
import os
import random
import sys

import pygame
from pygame import Surface
from pygame.sprite import Sprite

WIDTH = 1000
HEIGHT = 700
FPS = 60
player_speed = 5


def load_image(name, color_key=None) -> Surface:
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image


class Character(Sprite):
    def __init__(self):
        super().__init__(player_group)

        self.image = load_image('Character.png')
        self.rect = self.image.get_rect()

        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2

        self.change_x = 0
        self.change_y = 0
        self.hp = 500  # hp по умолчанию

    def update(self):
        for vil in villains:
            if pygame.sprite.collide_mask(self, vil):
                self.hp -= 1

        if self.hp <= 0:
            global game_running
            game_running = False
            self.hp = 500
            villains.clear()
            for sprt in villain_group:
                sprt.kill()

    def get_hp(self):
        return self.hp


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
        return 5


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

    def update(self):
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
            if pygame.sprite.collide_mask(self, attack):
                self.hp -= attack.damage()

    def go_left(self):
        # Сами функции будут вызваны позже из основного цикла
        self.change_x = player_speed
        self.rect.x += self.change_x  # Двигаем игрока по Х

    def go_right(self):
        # то же самое, но вправо
        self.change_x = -player_speed
        self.rect.x += self.change_x

    def go_up(self):
        # Сами функции будут вызваны позже из основного цикла
        self.change_y = player_speed
        self.rect.y += self.change_y  # Двигаем игрока по y

    def go_down(self):
        self.change_y = -player_speed
        self.rect.y += self.change_y


def draw_game(world_offset_x, world_offset_y, image):
    screen.fill((0, 0, 0))

    # Draw a grid to simulate the infinite world
    grid_size = 50
    for x in range(-grid_size, WIDTH + grid_size, grid_size):
        for y in range(-grid_size, HEIGHT + grid_size, grid_size):
            world_x = x + world_offset_x % grid_size
            world_y = y + world_offset_y % grid_size
            screen.blit(image, (world_x, world_y))

    font = pygame.font.Font(None, 36)
    title_text = font.render(str(character.get_hp()), True, (255, 255, 255))
    screen.blit(title_text, (10, 10))


def draw_menu():
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    title_text = font.render("Как игру назовем?", True, (0, 0, 0))
    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)

    # Draw Title
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 150))

    # Draw Start Button
    pygame.draw.rect(screen, (0, 255, 0), start_button)
    start_text = font.render("Start Game", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                             start_button.y + start_button.height // 2 - start_text.get_height() // 2))

    return start_button


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    bg_image = load_image('grass.png')
    clock = pygame.time.Clock()
    spell_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    villain_group = pygame.sprite.Group()
    grass = pygame.sprite.Group()
    character = Character()
    attack = Spell2()  # вид оружия/атаки в данный момент
    villains = []
    world_offset_x = 0
    world_offset_y = 0
    running = True
    game_running = False
    vil_count = 0
    vil_spawn_speed = 5000
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not game_running:
            # Draw the menu
            start_button = draw_menu()

            # Check for button clicks
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if start_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                game_running = True
                villains = [Villain() for i in range(6)]
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                for vil in villains:
                    vil.go_left()
                world_offset_x += player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                for vil in villains:
                    vil.go_right()
                world_offset_x -= player_speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                for vil in villains:
                    vil.go_up()
                world_offset_y += player_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                for vil in villains:
                    vil.go_down()
                world_offset_y -= player_speed

            vil_count += FPS / vil_spawn_speed
            if vil_count // 1 != 0:
                vil = Villain()
                villains.append(vil)
                vil_count = 0

            draw_game(world_offset_x, world_offset_y, bg_image)
            # all_sprites.draw(screen)
            # all_sprites.update()
            player_group.draw(screen)
            player_group.update()
            villain_group.draw(screen)
            villain_group.update()
            spell_group.draw(screen)
            spell_group.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
