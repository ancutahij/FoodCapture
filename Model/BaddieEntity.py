import pygame
from pygame.locals import  *

class Baddie(pygame.sprite.Sprite):
    #Simple Sprite
    def __init__(self, image, speed, surface ,rect = None, idImage= None):
        pygame.sprite.Sprite.__init__(self)
        self.idImage = idImage
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.speed = speed
        self.surface= surface
        self.rect = self.image.get_rect()
        if self.rect != None:
            self.rect = rect

    def get_x(self):
        """
            Get the top coordinate of the opposite candidate's rect
        """
        return self.rect.top

    def get_y(self):
        """
            Get the left coordinate of the opposite candidate's  rect
        """
        return self.rect.left

    def set_x(self, X):
        """
            Set the top coordinate of the opposite candidate  rect's to a given value
        """
        self.rect.top = X


    def set_y(self, Y):
        """
            Set the left coordinate of the opposite candidate's rect to a given value
        """
        self.rect.left = Y

    def get_speed(self):

        return self.speed

    def get_surface(self):

        return self.surface

    def get_rect(self):
        return self.rect

    def setLeftRight(self):
        """
            The first argument of move_ip moves  the  player to right  if pixels > 0, otherwise to left.
            The second argument moves the player object down if pixels>0, otherwise top

            For example:
            move_ip(-5, -15) would move the Rect object 5 pixels to the left and 15 pixels up

        """
        self.rect.move_ip(0, self.speed)

    def get_idImage(self):
        return self.idImage