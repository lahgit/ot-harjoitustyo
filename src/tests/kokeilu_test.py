import unittest
import pygame
from level import Level

Level1 =   [[1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 0]]





class TestLevel(unittest.TestCase):

    def test_creating_squares(self):

        pygame.init()
        testdisplay = pygame.display.set_mode((500, 445))

        testlevel = Level(testdisplay, Level1)
        testlevel.draw_grid()
        
        self.assertEqual(testlevel.GenerationSuccess, True)

