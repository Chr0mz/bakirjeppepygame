import pygame
import random
import Game

class Menu:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 300
        self.height = 200
        self.tower_names = [] 
        self.imgs = []
        self.selected_tower = 0 

    def draw(self, surface):
        pass

    def create_tower(self, name):
        self.name = name
    
    def sell_tower(self, price):
        self.price = price

    def increase_round(self):
        rounds = 1
        dead = False
        if not dead:
            rounds = rounds + 1

    def resell(self):
        pass

    def reduce_lives_and_towers(self):
        randtowerremoval = random.randint(0, len(Game.game1.towers)) #Tower amount        
        
    def enemy_generation(self):
        pass

    def run(self):
        pass
    
    def collide(self):
        pass

