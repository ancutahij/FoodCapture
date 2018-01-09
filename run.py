import os

from Controller.Logic import KeyBoard
from Controller.readWriteFile import TopScore
from Model.BaddieRepository import BaddieRepository
from Model.Images import ImagesRepository
from Model.PlayerEntity import Player
from View.Graphic import GraphicalView
from View.Menu import Menu


def getImagePath():
    """
        Return the path of  images folder.
    """
    currentPath = os.path.dirname(__file__)
    resourcesPath = os.path.join(currentPath, "Resources")
    imagesPath = os.path.join(resourcesPath, "Images")
    return imagesPath

player = Player(os.path.join(getImagePath(), "stay.png"),os.path.join(getImagePath(), "right.png"), os.path.join(getImagePath(), "left.png"))
player.set_x(510)
player.set_y(280)
allBaddies = BaddieRepository(ImagesRepository())
view = GraphicalView()
topScoreFile = TopScore("Resources/topScore.txt")
menuView = Menu()
KeyBoard(player, allBaddies, view,topScoreFile, menuView)



