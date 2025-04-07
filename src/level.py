import pygame


class Level:
    def __init__(self, display, level_map):

        self.display = display
        self.level_map = level_map
        self.tileSize = 50
        self.GenerationSuccess = False
        self.tile_texture = pygame.image.load("src/tiletexture.png")
        self.flag_texture = pygame.image.load("src/flagtexture.png")
        self.tile_texture = pygame.transform.scale(
            self.tile_texture, (self.tileSize, self.tileSize))
        self.flag_texture = pygame.transform.scale(
            self.flag_texture, (self.tileSize, self.tileSize))

    def draw_grid(self):  # Osittain generoitua koodia ChatGPT:llä

        for row in range(len(self.level_map)):

            for col in range(len(self.level_map[row])):

                x = col * self.tileSize
                y = row * self.tileSize + 60

                if self.level_map[row][col] == 1:
                    self.display.blit(self.flag_texture, (x, y))
                if self.level_map[row][col] == 0:
                    self.display.blit(self.tile_texture, (x, y))
                # Ja tähän loppuu ChatGPT:een koodi

        self.GenerationSuccess = True
