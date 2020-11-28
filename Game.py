import pygame
import random
import menu
import enemyTemplate
import towerTemplate
import os

pygame.init()

class Game():
    def __init__(self):
        self.width = 1080
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 250
        #self.background = pygame.image.load('./assets/background/background.png')
        self.background = pygame.image.load(os.path.join('assets', 'enemies', '1', 'enemy1.png'))

    def run(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.update()

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
        randtowerremoval = random.randint(0, len(self.towers)) #Tower amount        
    
    def enemy_generation(self):
        pass
    
    def collide(self):
        pass



game1 = Game()
game1.draw()
game1.run()
