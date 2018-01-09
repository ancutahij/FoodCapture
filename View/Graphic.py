import os
import pygame

class GraphicalView:
    def __init__(self):

        self.WINDOWWIDTH = 600
        self.WINDOWHEIGHT = 600
        self.TEXTCOLOR = (255, 255, 255)
        self.BACKGROUNDCOLOR = (200, 25, 0)
        self.FPS = 60
        self.windowSurface = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))

        # Set up the fonts.
        pygame.init()
        self.font = pygame.font.SysFont(None, 48)


    def get_width(self):
        return self.WINDOWWIDTH

    def get_height(self):
        return self.WINDOWHEIGHT


    def drawText(self, text, x, y, surface=None ):
        """
            Draw the text onto the window screen.
        """
        if surface == None:
            surface = self.windowSurface
        textobj = self.font.render(text, 1, self.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def drawsPlayer(self,  playerImage=None, playerRect=None):
        # Draw the player's rectangle.
        self.windowSurface.blit(playerImage, playerRect)

    def drawsBaddies(self, baddieSurface=None, baddieRect=None):
        # Draw each baddie.
        self.windowSurface.blit(baddieSurface, baddieRect)


    def getImagePath(self):
        """
            Return the path of images folder.
        """
        # currentPath = os.path.join( os.path.dirname( __file__ ), '..' )
        one_folder_up = os.getcwd()
        resourcesPath = os.path.join(one_folder_up, "Resources")
        imagesPath = os.path.join(resourcesPath, "Images")
        return imagesPath

    def setUp(self, nrLife):
        pygame.init()
        # Draw the game world on the window
        imagesPath = self.getImagePath()
        img = pygame.image.load(os.path.join(imagesPath, "forest.png"))
        self.windowSurface.blit(img, (0,0))

        # Set up  the window, and the mouse cursor.
        pygame.display.set_caption("FoodCapture")
        pygame.mouse.set_visible(True)

        #Draw the life indicator
        lifePath = os.path.join(imagesPath,  "life.png")
        lifeImage = pygame.image.load(lifePath)
        lifeImage = pygame.transform.scale(lifeImage, (49, 49))
        for i in range(nrLife):
            self.windowSurface.blit(lifeImage, (600-(i+1)*50, 2))


        #Draw the player's road
        for i in range(15):
            pygame.draw.rect(self.windowSurface, (51, 26, 0),  (i*50 +i ,570,   50, 30))


