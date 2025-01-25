import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60
player_speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

spell_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
villain_group = pygame.sprite.Group()
