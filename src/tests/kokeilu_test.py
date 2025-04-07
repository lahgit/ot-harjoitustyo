import unittest
import pygame
from level import Level
from levelselect import SelectorForLevels
from unittest.mock import patch


Level1 = [[1, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0],
          [1, 1, 1, 1, 1, 0, 0, 0]]


Level2 = [[1, 1, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0]]

Level3 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]


Levellist = {"Level 1": Level1, "Level 2": Level2, "Level 3": Level3}

class TestLevel(unittest.TestCase):

    def test_creating_squares(self):

        pygame.init()
        testdisplay = pygame.display.set_mode((500, 445))

        testlevel = Level(testdisplay, Level1)
        testlevel.draw_grid()

        self.assertEqual(testlevel.GenerationSuccess, True)

    def test_selecting_level(self):
        with patch('builtins.input', return_value='2'):
            Testingclass = SelectorForLevels()
            answer = Testingclass.select()
        

            self.assertEqual(answer, Level2)
