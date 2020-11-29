import pygame

class Enemy:
    images = []

    def __init__(self, x, y, width, height):
        self.x = None
        self.y = None
        self.width = width
        self.height = height
        self.speed = 0
        self.health = 20
        self.path = [(39, 163), (153, 159), (377, 157), (593, 157), (827, 157), (1000, 156), (1035, 403), (614, 382), (82, 371), (58, 615), (288, 602), (527, 613),
                             (817, 599), (1042, 606), (1033, 724), (1035, 839), (838, 827), (557, 821), (389, 824), (183, 808), (27, 809)]
        self.path_position = 0
        self.imgs = []
        self.animation_count = 0

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

    def move(self, change):
        """
        Will move enemy.
        return None
        """
        pass
        x_1, y_1 = self.path[self.path_position]
        if self.path_position + 1 >= len(self.path):
            x_2, y_2 = (-15, 809)
        else:
            x_2, y_2 = self.path[self.path_position+1]
        
        change_x = x_2 - x_1
        change_y = y_2 - y_1


    def hit(self):
        """
        Will return if an enemy has died and will remove a hitpoint.
        :return: Bool
        """

        self.health -= 1
        if self.health <= 0:
            return True


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
        self.move(1)


