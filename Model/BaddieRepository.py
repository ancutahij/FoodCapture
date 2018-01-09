from random import randint, choice

import pygame

from Model.BaddieEntity import Baddie


class BaddieRepository:
    """
        A simple class that contains a group with all Sprites(baddies).
    """
    def __init__(self, images):
        self.allBaddies= pygame.sprite.Group() # storing all Sprites in a group for a better flexibility
        self.allImages = images
        self.ADDNEWBADDIERATE = 10
        self.BADDIESIZE=40
        self.BADDIEMINSPEED =3
        self.BADDIEMAXSPEED =5


    def addNewBaddie(self, numberBaddiesOnScreen, WINDOWWIDTH, score, baddieAddCounter, getLife=None):
        """
            Add new baddie at the top of the screen, if needed
        """


        if numberBaddiesOnScreen < self.ADDNEWBADDIERATE and baddieAddCounter %10 ==0 :

            images= self.allImages.get_all()
            if score%25 == 0 and score!= 0 and getLife !=score:  # every multiple score of 25 generates a new life :)
                baddieImage = images[22]
                getLife =score
            else:
                baddieImage = choice(images[:21])

            baddieImagePath= baddieImage.get_path()
            baddieSpeed = randint(self.BADDIEMINSPEED + score//25, self.BADDIEMAXSPEED +score//25)
            baddieSurface =  pygame.transform.scale(pygame.image.load(baddieImagePath),(50, 50))
            baddieRect =  pygame.Rect(randint(0, WINDOWWIDTH - self.BADDIESIZE), 0-self.BADDIESIZE,self.BADDIESIZE, self.BADDIESIZE)
            baddie = Baddie(baddieImagePath, baddieSpeed, baddieSurface,baddieRect , baddieImage.get_id() )
            self.allBaddies.add (baddie)

        return getLife

    def get_all(self):
        return self.allBaddies

    def clearGroup(self):
        """
            Clear the baddies group by removing every element
        """
        allBaddies = self.get_all()
        for b in allBaddies:
            b.kill()