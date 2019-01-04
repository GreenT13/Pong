import pygame
from framework.states.AbstractState import AbstractState
from framework.states.Transition import Transition, TransitionConstants


class FirstState(AbstractState):
    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.font.init()

        # The first real state.
        self.nextTransition = Transition(TransitionConstants.MAIN_MENU, False)

    def update(self, delta):
        pass

    def draw(self, interpolation):
        pass

    def handleEvent(self, event):
        pass

    def actionAfterEvent(self):
        pass
