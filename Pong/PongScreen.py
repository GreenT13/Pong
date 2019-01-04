import pygame


class PongScreen:
    def __init__(self):
        # Resizable (https://stackoverflow.com/questions/29453587/how-do-you-start-pygame-window-maximized?rq=1)
        # screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.positionX = float(self.width / 2)
        self.positionY = float(self.height / 2)
        self.speed = 400  # Number of pixels per second.
        pygame.font.init()

    def draw(self, interpolation):
        # Clear the screen before drawing it again.
        self.screen.fill(0)

        # Draw everything.
        pygame.draw.rect(self.screen, pygame.color.Color('blue'), (self.positionX, self.positionY, 10, 10))

        # Update the screen.
        pygame.display.flip()

    def moveLeft(self, dt):
        self.positionX += self.speed * dt
        if self.positionX + 10 > self.width or self.positionX < 0:
            # We reached either left or right end, so we switch speed.
            self.speed *= -1
