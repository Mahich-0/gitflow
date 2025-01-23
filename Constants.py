import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60
player_speed = 5
tm = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
villains = []

spell_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
villain_group = pygame.sprite.Group()

running = True
game_running = False