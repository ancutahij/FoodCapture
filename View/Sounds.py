import os
import pygame


class SoundMusic:
    @staticmethod
    def getImagePath():
        """
            Return the path of music folder.
        """
        one_folder_up = os.getcwd()
        resourcesPath = os.path.join(one_folder_up, "Resources")
        musicPath = os.path.join(resourcesPath, "Sounds")
        return musicPath


    @staticmethod
    def startMusic(identificator):
        """
            Starts a sound after an identificator (ie sound's name)
        """
        musicPath = SoundMusic.getImagePath()
        if identificator == "yuck":
            pickUpSound = pygame.mixer.Sound(os.path.join(musicPath, "yuck.wav"))
            pickUpSound.play()
        elif identificator== "chewing":
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(musicPath, "chewing.wav"))
            pygame.mixer.music.play()
        elif identificator == "yes":
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(musicPath, "yes.wav"))
            pygame.mixer.music.play()
        elif identificator == "gameOver":
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join(musicPath, "gameOver.wav"))
            pygame.mixer.music.play()

