import pygame


class Level:
    def __init__(self, display, level_map):

        self.display = display
        self.level_map = level_map
        self.tileSize = 50
        self.GenerationSuccess = False
        self.tile_texture = pygame.image.load("tiletexture.png")
        self.flag_texture = pygame.image.load("flagtexture.png")
        self.tile_texture = pygame.transform.scale(self.tile_texture, (self.tileSize, self.tileSize))
        self.flag_texture = pygame.transform.scale(self.flag_texture, (self.tileSize, self.tileSize))
        

    def draw_grid(self): #Osittain generoitua koodia ChatGPT:llä
        #gapy = 0
        for row in range(len(self.level_map)):
            #gapx = 0
            #gapy += 5
            for col in range(len(self.level_map[row])):
                #gapx += 5
                x = col * self.tileSize #+ gapx
                y = row * self.tileSize + 60 #+ gapy 

                if self.level_map[row][col] == 1:
                    self.display.blit(self.flag_texture, (x, y))
                if self.level_map[row][col] == 0:
                    self.display.blit(self.tile_texture, (x, y))
                #pygame.draw.rect(self.display, (20, 20, 20), (x, y, self.tileSize, self.tileSize), 2) #Ja tähän loppuu ChatGPT:een koodi

    
        self.GenerationSuccess = True