import pygame
from level import Level
from levelselect import SelectorForLevels


def main():
    getlevel = SelectorForLevels()
    level_map = getlevel.selected_level
    height = len(level_map)
    width = len(level_map[0])
    topbar = 60
    display_height = height * 50 + topbar
    display_width = width * 50
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper")

    pygame.init()
    clock = pygame.time.Clock()

    level = Level(display, level_map)

    mouse_held = False

    KeepGameRunning = True
    while KeepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGameRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_held:  # generoitu koodi alkaa
            x, y = event.pos ## koodia kuitenkin paljon muokattu

            levelgrid_x = x // 50
            levelgrid_y = (y-topbar) // 50



            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # empty tile
                if level_map[levelgrid_y][levelgrid_x] == 99:
                    level_map[levelgrid_y][levelgrid_x] = 9


            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 1
                if level_map[levelgrid_y][levelgrid_x] == 11:
                    level_map[levelgrid_y][levelgrid_x] = 1

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 2
                if level_map[levelgrid_y][levelgrid_x] == 22:
                    level_map[levelgrid_y][levelgrid_x] = 2

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 3
                if level_map[levelgrid_y][levelgrid_x] == 33:
                    level_map[levelgrid_y][levelgrid_x] = 3

            
            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 4
                if level_map[levelgrid_y][levelgrid_x] == 44:
                    level_map[levelgrid_y][levelgrid_x] = 4

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 5
                if level_map[levelgrid_y][levelgrid_x] == 55:
                    level_map[levelgrid_y][levelgrid_x] = 5

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 6
                if level_map[levelgrid_y][levelgrid_x] == 66:
                    level_map[levelgrid_y][levelgrid_x] = 6

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 7
                if level_map[levelgrid_y][levelgrid_x] == 77:
                    level_map[levelgrid_y][levelgrid_x] = 7

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height: # tile 8
                if level_map[levelgrid_y][levelgrid_x] == 88:
                    level_map[levelgrid_y][levelgrid_x] = 8

            mouse_held = True

        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not mouse_held:
            x, y = event.pos
            levelgrid_x = x // 50
            levelgrid_y = (y - topbar) // 50

            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height:
                current_value = level_map[levelgrid_y][levelgrid_x]
                
                if current_value == 10:
                    level_map[levelgrid_y][levelgrid_x] = 100
                elif current_value == 100:
                    level_map[levelgrid_y][levelgrid_x] = 10

                
                if current_value == 11:
                    level_map[levelgrid_y][levelgrid_x] = 111
                elif current_value == 111:
                    level_map[levelgrid_y][levelgrid_x] = 11

                
                if current_value == 22:
                    level_map[levelgrid_y][levelgrid_x] = 222
                elif current_value == 222:
                    level_map[levelgrid_y][levelgrid_x] = 22

                if current_value == 33:
                    level_map[levelgrid_y][levelgrid_x] = 333
                elif current_value == 333:
                    level_map[levelgrid_y][levelgrid_x] = 33

                if current_value == 44:
                    level_map[levelgrid_y][levelgrid_x] = 444
                elif current_value == 444:
                    level_map[levelgrid_y][levelgrid_x] = 44

                if current_value == 55:
                    level_map[levelgrid_y][levelgrid_x] = 555
                elif current_value == 555:
                    level_map[levelgrid_y][levelgrid_x] = 55

                
                if current_value == 66:
                    level_map[levelgrid_y][levelgrid_x] = 665
                elif current_value == 665:
                    level_map[levelgrid_y][levelgrid_x] = 66

                if current_value == 77:
                    level_map[levelgrid_y][levelgrid_x] = 777
                elif current_value == 777:
                    level_map[levelgrid_y][levelgrid_x] = 77

                if current_value == 88:
                    level_map[levelgrid_y][levelgrid_x] = 888
                elif current_value == 888:
                    level_map[levelgrid_y][levelgrid_x] = 88

                if current_value == 99:
                    level_map[levelgrid_y][levelgrid_x] = 999
                elif current_value == 999:
                    level_map[levelgrid_y][levelgrid_x] = 99

            mouse_held = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False  # generoitu koodi päättyy

        display.fill((120, 120, 120))
        display.fill((180, 180, 180), rect=(0, 0, display_width, 60))

        level.draw_grid()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
