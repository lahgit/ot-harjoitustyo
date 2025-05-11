import unittest
import pygame
from level import Level
from levelselect import UI
import levelselect
from unittest.mock import patch
import time
from tkinter import Tk, ttk, StringVar





class TestUI(unittest.TestCase):

    def test_button_2(self):

        
        levelselect.selected_level_value_global = 0

        window = Tk()
        window.title("Level select")

        ui = UI(window)
        ui.start()

        ui._choose2()

        #time.sleep(2)

        self.assertEqual(levelselect.selected_level_value_global, 2)


    def test_button_1(self):

        
        levelselect.selected_level_value_global = 0

        window = Tk()
        window.title("Level select")

        ui = UI(window)
        ui.start()

        ui._choose1()

        #time.sleep(2)

        self.assertEqual(levelselect.selected_level_value_global, 1)


    def test_button_3(self):

        
        levelselect.selected_level_value_global = 0

        window = Tk()
        window.title("Level select")

        ui = UI(window)
        ui.start()

        ui._choose3()

        #time.sleep(2)

        self.assertEqual(levelselect.selected_level_value_global, 3)

    
