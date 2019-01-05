import pygame
from framework.states.AbstractState import AbstractState
from pong import PongGlobalVariables


class Pong(AbstractState):
    def __init__(self):
        super().__init__()

        self.screen = PongGlobalVariables.screen

        # The ball
        self.ballPosition = [100.0, 100.0]  # [x,y] position
        self.ballVelocity = [1.0, 0.0]  # Vector indicating [horizontal pixels per second, vertical pixels per second]

        # The players
        self.playerLeftPosition = float(PongGlobalVariables.height / 2)
        self.playerRightPosition = float(PongGlobalVariables.height / 2)

        # For testing
        self.positionX = float(PongGlobalVariables.width / 2)
        self.positionY = float(PongGlobalVariables.height / 2)
        self.speed = 400  # Number of pixels per second.

    def update(self, delta):
        self.positionX += self.speed * delta
        if self.positionX + 10 > PongGlobalVariables.width or self.positionX < 0:
            # We reached either left or right end, so we switch speed.
            self.speed *= -1

    def draw(self, interpolation):
        # Clear the screen before drawing it again.
        self.screen.fill(0)

        # Draw everything.
        pygame.draw.rect(self.screen, pygame.color.Color('blue'), (self.positionX, self.positionY, 10, 10))

    def handleEvent(self, event):
        pass

    def actionAfterEvent(self):
        pass

