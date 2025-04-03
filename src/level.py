import pygame


class Level:
    def __init__(self, display, level_map):

        self.display = display
        self.level_map = level_map
        self.tileSize = 50
        self.GenerationSuccess = False
        self.horizontalTotalGap = 0
        self.verticalTotalGap = 0
        

    def draw_grid(self): #Osittain generoitua koodia ChatGPT:llä
        gapy = 0
        for row in range(len(self.level_map)):
            gapx = 0
            gapy += 5
            for col in range(len(self.level_map[row])):
                gapx += 5
                x = col * self.tileSize + gapx
                y = row * self.tileSize + 60 + gapy 

                if self.level_map[row][col] == 1:
                    color = (80, 50, 50)
                else:
                    color = (200, 200, 200)

                pygame.draw.rect(self.display, color, (x, y, self.tileSize, self.tileSize))
                pygame.draw.rect(self.display, (0, 0, 0), (x, y, self.tileSize, self.tileSize), 2) #Ja tähän loppuu ChatGPT:een koodi

        self.horizontalTotalGap = gapx
        self.verticalTotalGap = gapy
        self.GenerationSuccess = True