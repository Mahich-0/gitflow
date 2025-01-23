from Constants import *
from Render import draw_game, draw_menu
from Enemies import Villain
from ImageLoad import load_image

if __name__ == '__main__':
    pygame.init()
    bg_image = load_image('grass.png')
    clock = pygame.time.Clock()
    grass = pygame.sprite.Group()
    world_offset_x = 0
    world_offset_y = 0
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
                tm = 0
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
            player_group.draw(screen)
            player_group.update()
            villain_group.draw(screen)
            villain_group.update()
            spell_group.draw(screen)
            spell_group.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
