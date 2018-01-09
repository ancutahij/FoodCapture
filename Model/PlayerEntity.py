import pygame


class Player(pygame.sprite.Sprite):
    #Simple player object
    def __init__(self, image1, image2, image3):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
        self.image3 = pygame.image.load(image3)
        self.image1 = pygame.transform.scale(self.image1, (60, 60))
        self.image2 = pygame.transform.scale(self.image2, (60, 60))
        self.image3 = pygame.transform.scale(self.image3, (60, 60))
        self.rect = self.image1.get_rect()

    def get_x(self):
        """
            Get the top coordinate of player rect
        """
        return self.rect.top

    def get_y(self):
        """
            Get the left coordinate of player rect
        """
        return self.rect.left

    def get_right(self):
        return self.rect.right

    def get_left(self):
        return self.rect.left

    def get_rect(self):
        return self.rect

    def set_x(self, X):
        """
            Set the top coordinate of player rect to a given value
        """
        self.rect.top = X

    def set_y(self, Y):
        """
            Set the left coordinate of player rect to a given value
        """
        self.rect.left = Y

    def setLeftRight(self, pixels):
        self.rect.move_ip(pixels, 0)