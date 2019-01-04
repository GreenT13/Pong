import pygame
from framework.process.Process import Process
from pong.PongScreen import PongScreen


class Pong:
    def __init__(self):
        # Variables that stay fixed during a game.
        self.pongScreen = PongScreen()

        # Variables that will change.
        # The screen

        # The ball
        self.ballPosition = [100.0, 100.0]  # [x,y] position
        self.ballVelocity = [1.0, 0.0]  # Vector indicating [horizontal pixels per second, vertical pixels per second]

        # The players
        self.playerLeftPosition = float(self.pongScreen.height / 2)
        self.playerRightPosition = float(self.pongScreen.height / 2)

    def start(self):
        game = Process(
            update=self.updateLogic,
            draw=self.pongScreen.draw,
            handleEvent=self.handleEvent
        )
        game.startProcess()

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()

    def updateLogic(self, delta):
        self.pongScreen.moveLeft(delta)
