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
        
        if event.type == pygame.MOUSEBUTTONDOWN and not mouse_held: # osittain generoitua ChatGPTeellä
            x, y = event.pos

            levelgrid_x = x /  50
            levelgrid_y = (y-topbar) /  50

            levelgrid_x = int(levelgrid_x)
            levelgrid_y = int(levelgrid_y)


            if 0 <= levelgrid_x < width and 0 <= levelgrid_y < height:
                level_map[levelgrid_y][levelgrid_x] = 1 if level_map[levelgrid_y][levelgrid_x] == 0 else 0
                
            mouse_held = True 

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False # loppuu tähän

        display.fill((120, 120, 120)) 
        display.fill((180, 180, 180), rect = (0, 0, display_width, 60))

        level.draw_grid()

        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()