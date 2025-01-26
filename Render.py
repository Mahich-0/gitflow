from Globals import *
from Char import character


def draw_game(world_offset_x, world_offset_y, image, tm, cast, spell1_cast, spell2_cast, spell3_cast):
    screen.fill((0, 0, 0))

    # Draw a grid to simulate the infinite world
    grid_size = 50
    for x in range(-grid_size, WIDTH + grid_size, grid_size):
        for y in range(-grid_size, HEIGHT + grid_size, grid_size):
            world_x = x + world_offset_x % grid_size
            world_y = y + world_offset_y % grid_size
            screen.blit(image, (world_x, world_y))

    font = pygame.font.Font(None, 36)
    text = font.render(str(character.hp), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    text = font.render(str(int(tm)) + " сек.", True, (255, 255, 255))
    screen.blit(text, (10, 50))

    text = font.render('First cast: ' + ''.join(spell1_cast), True, (255, 255, 255))
    screen.blit(text, (10, 75))

    text = font.render('Second cast: ' + ''.join(spell2_cast), True, (255, 255, 255))
    screen.blit(text, (10, 100))

    text = font.render('Third cast: ' + ''.join(spell3_cast), True, (255, 255, 255))
    screen.blit(text, (10, 125))

    text = font.render(''.join(cast), True, (255, 255, 255))
    screen.blit(text, (10, 150))

    text = font.render(str(character.kills_count), True, (255, 255, 255))
    screen.blit(text, (10, 175))


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
