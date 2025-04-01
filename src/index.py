import pygame




Level1 =   [[1, 1, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0]]

tileSize = 50

def draw_grid(display, level_map):
    gapy = 0
    for row in range(len(level_map)):
        gapx = 0
        gapy += 5
        for col in range(len(level_map[row])):
            gapx += 5
            x = col * tileSize + gapx
            y = row * tileSize + 60 + gapy 

            if level_map[row][col] == 1:
                color = (50, 50, 50)
            else:
                color = (200, 200, 200)

            pygame.draw.rect(display, color, (x, y, tileSize, tileSize))
            pygame.draw.rect(display, (0, 0, 0), (x, y, tileSize, tileSize), 2)



def main():
    level_map = Level1
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * 50 + 100
    display_width = width * 50 + 45
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper")

    pygame.init()
    clock = pygame.time.Clock()


    KeepGameRunning = True
    while KeepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGameRunning = False  

        display.fill((120, 120, 120)) 
        display.fill((180, 180, 180), rect = (0, 0, 500, 60))

        draw_grid(display, Level1)

        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()