import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60
player_speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

base_group = pygame.sprite.Group()
spell1_group = pygame.sprite.Group()
spell2_group = pygame.sprite.Group()
spell3_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
villain_group = pygame.sprite.Group()
