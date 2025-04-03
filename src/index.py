import pygame
from level import Level
from levelselect import SelectorForLevels



def main():
    getlevel = SelectorForLevels()
    level_map = getlevel.selected_level
    height = len(level_map)
    width = len(level_map[0])
    topbar = 60
    display_height = height * 55.5 + topbar
    display_width = width * 55.5
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper")

    pygame.init()
    clock = pygame.time.Clock()

    level = Level(display, level_map)


    KeepGameRunning = True
    while KeepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGameRunning = False  

        display.fill((120, 120, 120)) 
        display.fill((180, 180, 180), rect = (0, 0, display_width, 60))

        level.draw_grid()

        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()