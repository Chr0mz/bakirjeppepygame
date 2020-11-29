import pygame
import random
import menu
import enemyTemplate
import towerTemplate
import os

pygame.init()

heartimg = os.path.join('assets', 'randomstuff', 'HeartImg.png')
pause_menu = os.path.join('assets', 'Pause menu.png')

path = [(39, 163),
(153, 159),
(377, 157),
(593, 157),
(827, 157),
(1000, 156),
(1035, 403),
(614, 382),
(82, 371),
(58, 615),
(288, 602),
(527, 613),
(817, 599),
(1042, 606),
(1033, 724),
(1035, 839),
(838, 827),
(557, 821),
(389, 824),
(183, 808),
(27, 809)]

class Game():
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 250
        self.background = pygame.image.load(os.path.join('assets', 'Map', 'Backround.JPG'))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))


    def run(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                position = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw()
        pygame.quit()

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
game1.run()
