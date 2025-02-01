from Globals import *
from Char import character


def draw_game(world_offset_x, world_offset_y, image, tm, cast, spell1_cast, spell2_cast, spell3_cast):
    screen.fill((0, 0, 0))

    min = 0
    tm = int(tm)
    while tm >= 60:
        min += 1
        tm %= 60

    # Draw a grid to simulate the infinite world
    grid_size = 50
    for x in range(-grid_size, WIDTH + grid_size, grid_size):
        for y in range(-grid_size, HEIGHT + grid_size, grid_size):
            world_x = x + world_offset_x % grid_size
            world_y = y + world_offset_y % grid_size
            screen.blit(image, (world_x, world_y))

    font = pygame.font.Font(None, 36)

    text = font.render(str(min) + ':' + str(tm), True, (255, 255, 255))
    screen.blit(text, (470, 35))

    text = font.render('hp: ' + str(character.hp), True, (255, 255, 255))
    screen.blit(text, (910, 10))

    text = font.render('kills: ' + str(character.kills_count), True, (255, 255, 255))
    screen.blit(text, (910, 35))

    kills_before_spell1 = ''
    if character.kills_count < 10:
        kills_before_spell1 = f'{character.kills_count}/10'
    text = font.render('First cast: ' + ''.join(spell1_cast) + kills_before_spell1, True, (255, 255, 255))
    screen.blit(text, (10, 10))

    kills_before_spell2 = ''
    if character.kills_count < 20:
        kills_before_spell2 = f'{character.kills_count}/20'
    text = font.render('Second cast: ' + ''.join(spell2_cast) + kills_before_spell2, True, (255, 255, 255))
    screen.blit(text, (10, 35))

    kills_before_spell3 = ''
    if character.kills_count < 30:
        kills_before_spell3 = f'{character.kills_count}/30'
    text = font.render('Third cast: ' + ''.join(spell3_cast) + kills_before_spell3, True, (255, 255, 255))
    screen.blit(text, (10, 60))

    text = font.render(''.join(cast), True, (255, 255, 255))
    screen.blit(text, (10, 85))


def draw_menu():
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    title_text = font.render("Judgement Cut End", True, (0, 0, 0))
    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)

    # Draw Title
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 150))

    # Draw Start Button
    pygame.draw.rect(screen, (0, 255, 0), start_button)
    start_text = font.render("Start Game", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                             start_button.y + start_button.height // 2 - start_text.get_height() // 2))

    return start_button


def restart_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    title_text = font.render("Game over!", True, (255, 255, 255))
    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)

    # Draw Title
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 150))

    # Draw Start Button
    pygame.draw.rect(screen, (0, 255, 0), start_button)
    start_text = font.render("Restart?", True, (255, 255, 255))
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                             start_button.y + start_button.height // 2 - start_text.get_height() // 2))

    return start_button
