import unittest
import pygame
from level import Level
from levelselect import UI
from unittest.mock import patch




Level1 = [[10, 22, 99, 99, 99, 99, 99, 99],
          [10, 33, 99, 11, 11, 11, 99, 99],
          [10, 22, 99, 11, 10, 22, 11, 11],
          [22, 22, 11, 11, 11, 22, 10, 11],
          [11, 10, 11, 11, 11, 22, 11, 11],
          [11, 11, 11, 11, 10, 22, 11, 11],
          [11, 22, 11, 33, 22, 33, 10, 11],
          [10, 22, 10, 22, 10, 22, 11, 11]]

level1mines = 11
level1tiles = 53



Level2 = [[10, 22, 10, 11, 11, 22, 10],
          [22, 33, 11, 11, 11, 10, 22],
          [10, 22, 11, 11, 22, 11, 11],
          [10, 22, 11, 10, 11, 99, 99]]

level2mines = 7
level2tiles = 21

Level3 = [[10, 10, 10, 22, 99, 11, 10, 10, 22, 10, 22, 10],
          [10, 66, 10, 22, 99, 22, 33, 33, 22, 11, 22, 11],
          [10, 44, 22, 22, 99, 11, 10, 11, 99, 99, 99, 99],
          [11, 22, 10, 11, 99, 11, 11, 11, 99, 99, 99, 99]]

level3mines = 12
level3tiles = 36


Levellist = {"Level 1": Level1, "Level 2": Level2, "Level 3": Level3}

class TestLevel(unittest.TestCase):

    def test_creating_squares(self):

        global selected_level_value_global
        selected_level_value_global = "1"

        pygame.init()
        testdisplay = pygame.display.set_mode((500, 445))

        testlevel = Level(testdisplay, Level1)
        testlevel.draw_grid()

        self.assertEqual(testlevel.GenerationSuccess, True)

    #def test_selecting_level(self):
    #    with patch('builtins.input', return_value='2'):
    #        Testingclass = SelectorForLevels()
    #        answer = Testingclass.select()
    #    
    #
    #        self.assertEqual(answer, Level2)
