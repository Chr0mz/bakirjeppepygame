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
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 250
        self.background = pygame.image.load('./assets/background/background.png')

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


game1 = Game()
game1.run()
