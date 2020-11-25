import pygame

class Enemy:
    images = pygame.image.load('./assets/enemies/')

    def __init__(self, x, y, width, height):
        self.x = None
        self.y = None
        self.width = width
        self.height = height
        self.speed = 0
        self.health = 20
        self.path = []
        self.imgs = None
        self.animation_count = 0

    def draw(self, window):
        """
        Draws enemies with a given image
        :param window: surface
        :return: None
        """
        self.animation_count += 1
        self.imgs = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animationcount = 0

        window.blit(self.imgs, (self.x, self.y))
        self.move()


    def collide(self, x, y):
        """
        Will return if the position has hit enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
            return False

    def move(self):
        """
        Will move enemy.
        return None
        """

    def hit(self):
        """
        Will return if an enemy has died and will remove a hitpoint.
        :return: Bool
        """

        self.health -= 1
        if self.health <= 0:
            return True


