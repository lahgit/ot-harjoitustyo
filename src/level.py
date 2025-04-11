import pygame


class Level:
    def __init__(self, display, level_map):

        self.display = display
        self.level_map = level_map
        self.tileSize = 50
        self.GenerationSuccess = False
        self.tile_texture = pygame.image.load("src/textures/tiletexture.png")
        self.flag_texture = pygame.image.load("src/textures/flagtexture.png")


        self.empty_texture = pygame.image.load("src/textures/empty.png")

        self.empty_texture = pygame.transform.scale(
            self.empty_texture, (self.tileSize, self.tileSize))
        
        self.one_texture = pygame.image.load("src/textures/number1.png")

        self.one_texture = pygame.transform.scale(
            self.one_texture, (self.tileSize, self.tileSize))
        

        self.two_texture = pygame.image.load("src/textures/number2.png")

        self.two_texture = pygame.transform.scale(
            self.two_texture, (self.tileSize, self.tileSize))
        
        self.three_texture = pygame.image.load("src/textures/number3.png")

        self.three_texture = pygame.transform.scale(
            self.three_texture, (self.tileSize, self.tileSize))
        

        self.four_texture = pygame.image.load("src/textures/number4.png")

        self.four_texture = pygame.transform.scale(
            self.four_texture, (self.tileSize, self.tileSize))
        
        self.five_texture = pygame.image.load("src/textures/number5.png")

        self.five_texture = pygame.transform.scale(
            self.five_texture, (self.tileSize, self.tileSize))
        
        self.six_texture = pygame.image.load("src/textures/number6.png")

        self.six_texture = pygame.transform.scale(
            self.six_texture, (self.tileSize, self.tileSize))
        
        self.seven_texture = pygame.image.load("src/textures/number7.png")

        self.seven_texture = pygame.transform.scale(
            self.seven_texture, (self.tileSize, self.tileSize))
        
        self.eight_texture = pygame.image.load("src/textures/number8.png")

        self.eight_texture = pygame.transform.scale(
            self.eight_texture, (self.tileSize, self.tileSize))
        

        self.tile_texture = pygame.transform.scale(
            self.tile_texture, (self.tileSize, self.tileSize))
        self.flag_texture = pygame.transform.scale(
            self.flag_texture, (self.tileSize, self.tileSize))
        
        self.unseentiles = [10, 11, 22, 33, 44, 55, 66, 77, 88, 99]
        self.flagged = [000, 100, 111, 222, 333, 444, 555, 665, 777, 888]

    def draw_grid(self):  # Osittain generoitua koodia ChatGPT:llä

        for row in range(len(self.level_map)):

            for col in range(len(self.level_map[row])):

                x = col * self.tileSize
                y = row * self.tileSize + 60

                if self.level_map[row][col] == 9:
                    self.display.blit(self.empty_texture, (x, y))

                if self.level_map[row][col] == 1:
                    self.display.blit(self.one_texture, (x, y))

                if self.level_map[row][col] == 2:
                    self.display.blit(self.two_texture, (x, y))

                if self.level_map[row][col] == 3:
                    self.display.blit(self.three_texture, (x, y))

                
                if self.level_map[row][col] == 4:
                    self.display.blit(self.four_texture, (x, y))

                if self.level_map[row][col] == 5:
                    self.display.blit(self.five_texture, (x, y))

                if self.level_map[row][col] == 6:
                    self.display.blit(self.six_texture, (x, y))

                if self.level_map[row][col] == 7:
                    self.display.blit(self.seven_texture, (x, y))

                if self.level_map[row][col] == 8:
                    self.display.blit(self.eight_texture, (x, y))



                if self.level_map[row][col] in self.unseentiles:#== 0:
                    self.display.blit(self.tile_texture, (x, y))
                # Ja tähän loppuu ChatGPT:een koodi

        self.GenerationSuccess = True
