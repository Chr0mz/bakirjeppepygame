import pygame
import os

class Menu:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 300
        self.height = 200
        self.tower_names = ['Archer Tower', 'Pyro Tower', 'Water Tower'] 
        self.imgs = [os.path.join('assets', 'Menu.png'), os.path.join('assets', 'Pause menu.png'), os.path.join('assets', 'Towers', 'Water Tower.png'), os.path.join('assets', 'Pyro Tower.png'), os.path.join('assets', 'Archer Tower.png')]
        self.selected_tower = 0

    def draw(self, surface):
        pass

    def click(self, x, y):
        """"
        Click somewhere
        :return: Bool
        """

    def click_menu(self, x, y):
        """
        Click on menu
        :return: String
        """
