import pygame, sys
from pygame.locals import  *

from View.Sounds import SoundMusic


class KeyBoard:
    def __init__(self, player, baddies, view,  topScoreFile, menuView):
        self.PLAYERMOVERATE = 6
        self.FPS= 60
        self.player = player
        self.baddies = baddies
        self.view = view
        self.topScoreFile = topScoreFile
        self.menuView = menuView
        self.moveRight = False
        self.moveLeft = False
        self.numberLife = 3
        self.HOVER = False
        self.BUTTONS = [pygame.Rect(185,290,250,60), pygame.Rect(185,390,250,60) ]
        self.menuRun()


    def playerHasHitBaddie(self, baddies, score):

      for b in baddies:

          if pygame.sprite.collide_rect(self.player, b):
              imgId = b.get_idImage()
              image = self.baddies.allImages.getByID(imgId)
              score = score + image.get_value()
              if imgId==23 and self.numberLife<7: # we caught a life, we cannot have more than 5 lives :)
                  self.numberLife+=1
                  SoundMusic.startMusic("yes")
              if image.get_value()<0: # we caught a baddie
                  self.numberLife-=1
                  SoundMusic.startMusic("yuck")
              elif image.get_value()>0:
                  SoundMusic.startMusic("chewing")
              b.kill()

      return score



    def terminate(self):
        """
            The game ended when the program reached here.
        """
        pygame.quit()
        sys.exit()
    
    def run(self, WINDOWWIDTH=None, WINDOWWHEIGHT=None):
        """
            The brain of the game.
            The logic and arithmetics are happening here.
        """

        pygame.init()
        mainClock = pygame.time.Clock()
        self.view.setUp(self.numberLife)

        score = 0
        topScore = self.topScoreFile.getTopScore()
        getLife= 0
        while True:


            baddieAddCounter = 0
            while True:
                self.view.setUp(self.numberLife)
                baddieAddCounter += 1
                for event in pygame.event.get():

                    if event.type == QUIT:
                        self.terminate()

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.terminate()
                        if event.key == K_LEFT or event.key == K_a:
                            self.moveRight = False
                            self.moveLeft = True
                        if event.key == K_RIGHT or event.key == K_d:
                            self.moveLeft = False
                            self.moveRight = True


                    if event.type == KEYUP:
                        if event.key == K_LEFT or event.key == K_a:
                            self.moveLeft = False
                        if event.key == K_RIGHT or event.key == K_d:
                            self.moveRight = False


                #Add new baddie at the top of the screen, if neede
                allBaddies = self.baddies.get_all()
                getLife = self.baddies.addNewBaddie(len(allBaddies), WINDOWWIDTH, score ,baddieAddCounter, getLife)

                #Move the player around
                if self.moveLeft and self.player.get_left()-self.PLAYERMOVERATE >= 0:
                    self.player.setLeftRight(-1 *self.PLAYERMOVERATE)

                if self.moveRight and self.player.get_right()+self.PLAYERMOVERATE <= WINDOWWIDTH:
                    self.player.setLeftRight(self.PLAYERMOVERATE)


                # Move the baddies down.
                for b in allBaddies:
                    b.setLeftRight()


                #Delete the baddies that have fallen past the bottom.
                for b in allBaddies:
                    if b.get_x() >= WINDOWWHEIGHT - 70 :
                        b.kill() # deletes the Sprite  from all groups of Sprites


                #Draw the player and Sprites
                if self.moveLeft:
                    self.view.drawsPlayer( self.player.image3, self.player.rect)
                elif self.moveRight:
                    self.view.drawsPlayer( self.player.image2, self.player.rect)
                else:
                    self.view.drawsPlayer( self.player.image1, self.player.rect)

                for b in allBaddies :
                    self.view.drawsBaddies(b.get_surface(), b.get_rect())

                #Draw the current score
                self.view.drawText('Score: %s' % (score), 10, 0)
                if score> int(topScore):
                    topScore=score
                    self.topScoreFile.setNewTopScore(topScore)
                self.view.drawText('Top Score: %s' % (topScore), 10, 40)
                pygame.display.update()

                # Check if any of the baddies have hit the player.
                score = self.playerHasHitBaddie( allBaddies,score)

                mainClock.tick(self.FPS)

                if self.numberLife <0:
                    break
            break

        self.waitForPlayerToPressKey(score, topScore)


    def waitForPlayerToPressKey(self, score, topScore):
        """
            Waits for player to press any key for returning to the initial menu.
        """
        SoundMusic.startMusic("gameOver")
        while True:
            self.menuView.gameOverScreen(score, topScore)  # calling the Game Over Screen
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #Pressing ESC quits
                        self.terminate()
                    self.menuRun()

    def menuRun(self):
        pygame.init()
        mainClock = pygame.time.Clock()
        self.menuView.setUp(self.numberLife)
        self.HOVER=False
        self.menuView.drawButton(self.BUTTONS[0], "Play", flag=1)
        self.menuView.drawButton(self.BUTTONS[1], "Exit", flag=1)

        mouse_pos= (0,0)
        while True:
            if self.HOVER == False:
                self.menuView.drawButton(self.BUTTONS[0], "Play", flag=1)
                self.menuView.drawButton(self.BUTTONS[1], "Exit", flag=1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                mouse_pos = pygame.mouse.get_pos()

            for pos in range(2):

                if self.BUTTONS[pos].collidepoint(mouse_pos):
                    self.HOVER = True
                    if pos == 1:
                        self.menuView.drawButton(self.BUTTONS[pos], "Exit")
                    if pos == 0:
                        self.menuView.drawButton(self.BUTTONS[pos], "Play")
                else:
                    self.HOVER = False

                # The menu's buttons can be pressed only if the mouse's left button is pressed
                if self.BUTTONS[pos].collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pos == 1:
                        self.terminate()
                    else:
                        self.numberLife = 3
                        self.baddies.clearGroup()
                        self.run(self.view.get_width(), self.view.get_height())

            mainClock.tick(self.FPS)
            pygame.display.update()

