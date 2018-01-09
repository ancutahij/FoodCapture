import os
import pygame
import sys
from pygame.locals import  *
import time

class Menu:
    # A simple menu class
    def __init__(self):
        self.TEXTCOLOR = (255, 255, 255)
        self.WINDOWWIDTH = 600
        self.WINDOWHEIGHT = 600
        self.windowSurface = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))

        # Set up the fonts.
        pygame.init()
        self.font = pygame.font.SysFont(None, 48)
        self.fontTitle = pygame.font.SysFont(None, 110)

    def getImagePath(self):
        """
            Return the path of images folder.
        """

        one_folder_up = os.getcwd()
        resourcesPath = os.path.join(one_folder_up, "Resources")
        imagesPath = os.path.join(resourcesPath, "Images")
        return imagesPath

    def setUp(self, nrLife):
        pygame.init()

        # Draw the game world on the window
        imagesPath = self.getImagePath()
        img = pygame.image.load(os.path.join(imagesPath, "background.png"))
        self.windowSurface.blit(img, (0,0))

        # Set up  the window.
        pygame.display.set_caption("FoodCapture")

    def drawText(self, text, x,y,  font = None , surface=None,):
        """
            Draw the text onto the window screen.
        """
        if surface == None:
            surface = self.windowSurface
        if font == None:
            font = self.font
        textobj = font.render(text, 1, self.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def drawButton(self, buttonRect, Text, flag = None):
        """
            Draw the menu onto the screen
        """
        imagePath =self.getImagePath()
        if flag != None:
            img =  pygame.image.load(os.path.join(imagePath, "button.png"))
        else:
            img =  pygame.image.load(os.path.join(imagePath, "hover.png"))
        img = pygame.transform.scale(img, (250, 60))
        self.windowSurface.blit(img, buttonRect)
        self.drawText(Text,  buttonRect.left+90, buttonRect.top+13)

    def gameOverScreen(self, score=None, topScore=None):
        """
            The game over menu is displayed.
        """
        self.windowSurface.fill((0,0,0))
        self.drawText("Game Over!",  100, 100, self.fontTitle)

        self.drawText("Your score: {}".format(score),  190,220)
        self.drawText("Top score:   {}".format(topScore), 190, 270)
        self.drawText("Press any key to continue...", 90,380)