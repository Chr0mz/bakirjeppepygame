import pygame

class Enemy:
    def __init__(self):
        self.x = None
        self.y = None
        self.speed = 0
        self.health = 20
        self.path = []

    def picture(self):
        pass

    def collide(self, x, y):
        doesCollide = False

    def move(self, x, y):
        pass

    def hit(self):
        self.dmg = 5