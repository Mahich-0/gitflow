import random

from Render import draw_game, draw_menu
from Enemies import Villain
from Spells import *

if __name__ == '__main__':
    pygame.init()
    bg_image = load_image('grass.png')
    clock = pygame.time.Clock()
    grass = pygame.sprite.Group()
    base_group = pygame.sprite.Group()
    spell1_group = pygame.sprite.Group()
    spell2_group = pygame.sprite.Group()
    spell3_group = pygame.sprite.Group()
    villain_group = pygame.sprite.Group()
    world_offset_x = 0
    world_offset_y = 0
    villains = []
    vil_count = 0
    tm = 0
    spell1_update = -3
    spell2_update = -15
    spell3_update = -15
    cast_update = -0.2
    base = BazeAttack(base_group)
    spell1 = False
    spell2 = False
    spell3 = False
    spell1_cast = []
    spell2_cast = []
    spell3_cast = []
    running = True
    game_running = False
    cast = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_running = character.game_running

        if not game_running:
            # Draw the menu
            start_button = draw_menu()

            # Check for button clicks
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if start_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                game_running = True
                character.game_running = game_running
                villains = [Villain(villain_group) for i in range(6)]
                for spell in base_group:
                    spell.kill()
                for spell in spell1_group:
                    spell.kill()
                for spell in spell2_group:
                    spell.kill()
                base = BazeAttack(base_group)
                spell1 = False
                spell2 = False
                spell3 = False
                spell1_update = -3
                spell2_update = -15
                spell3_update = -15
                spell1_cast = []
                spell2_cast = []
                spell3_cast = []
                tm = 0
                cast = []
                cast_update = -0.2
                character.kills_count = 0
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                for vil in villains:
                    vil.go_left()
                for spell in spell1_group:
                    spell.go_left()
                for spell in spell3_group:
                    spell.go_left()
                world_offset_x += player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                for vil in villains:
                    vil.go_right()
                for spell in spell1_group:
                    spell.go_right()
                for spell in spell3_group:
                    spell.go_right()
                world_offset_x -= player_speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                for vil in villains:
                    vil.go_up()
                for spell in spell1_group:
                    spell.go_up()
                for spell in spell3_group:
                    spell.go_up()
                world_offset_y += player_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                for vil in villains:
                    vil.go_down()
                for spell in spell1_group:
                    spell.go_down()
                for spell in spell3_group:
                    spell.go_down()
                world_offset_y -= player_speed

            if keys[pygame.K_z]:
                if tm - cast_update > 0.2:
                    cast.append('z')
                    cast_update = tm
            if keys[pygame.K_x]:
                if tm - cast_update > 0.2:
                    cast.append('x')
                    cast_update = tm
            if keys[pygame.K_c]:
                if tm - cast_update > 0.2:
                    cast.append('c')
                    cast_update = tm
            if keys[pygame.K_e]:
                cast = []

            if character.kills_count >= 10 and spell1_cast == []:
                for _ in range(3):
                    spell1_cast.append(random.choice(['z', 'x', 'c']))

            if character.kills_count >= 20 and spell2_cast == []:
                for _ in range(3):
                    spell2_cast.append(random.choice(['z', 'x', 'c']))
                while spell1_cast == spell2_cast:
                    spell2_cast = []
                    for _ in range(3):
                        spell2_cast.append(random.choice(['z', 'x', 'c']))

            if character.kills_count >= 30 and spell3_cast == []:
                for _ in range(3):
                    spell3_cast.append(random.choice(['z', 'x', 'c']))
                while spell1_cast == spell3_cast or spell2_cast == spell3_cast:
                    spell3_cast = []
                    for _ in range(3):
                        spell3_cast.append(random.choice(['z', 'x', 'c']))

            if len(cast) == 3:
                if cast == spell1_cast and character.kills_count >= 10:
                    if tm - spell1_update > 3:
                        spell1 = Spell1(spell1_group)
                        spell1_update = tm
                        cast = []

                elif cast == spell2_cast and character.kills_count >= 20:
                    if tm - spell2_update > 15:
                        spell2 = Spell2(spell2_group)
                        spell2_update = tm
                        cast = []

                elif cast == spell3_cast and character.kills_count >= 30:
                    if tm - spell3_update > 15:
                        spell3 = Spell3(spell3_group)
                        spell3_update = tm
                        cast = []
                else:
                    cast = []

            if len(cast) > 3:
                cast = []

            if spell2:
                if tm - spell2_update >= 10:
                    spell2 = False

            if spell3:
                if tm - spell3_update >= 10:
                    spell3 = False

            vil_count += 1 / FPS
            if vil_count // 1 != 0:
                vil = Villain(villain_group)
                villains.append(vil)
                vil_count = 0

            tm += 1 / FPS

            draw_game(world_offset_x, world_offset_y, bg_image, tm, cast, spell1_cast, spell2_cast, spell3_cast)

            player_group.draw(screen)
            player_group.update(villains, villain_group)

            villain_group.draw(screen)
            villain_group.update(base, spell1, spell2, spell3)

            base_group.draw(screen)
            base_group.update()
            spell1_group.draw(screen)
            spell1_group.update(villains)
            spell2_group.draw(screen)
            spell2_group.update(tm - spell2_update)
            spell3_group.draw(screen)
            spell3_group.update(villains, tm - spell3_update)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
