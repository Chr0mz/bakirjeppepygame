import pygame
import menu
import WaterTower
import PyroTower
import ArcherTower

pygame.init()

class Game():
    def __init__(self):
        self.width = 800
        self.height = 600 
        self.window = pygame.display.set_mode(())
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 250    

    def run(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()



