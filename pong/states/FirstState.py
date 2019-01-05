import pygame
from framework.states.AbstractState import AbstractState
from framework.states.Transition import Transition, TransitionConstants
from pong import PongGlobalVariables


class FirstState(AbstractState):
    def __init__(self):
        super().__init__()

        # Initialize screen.
        PongGlobalVariables.screen = pygame.display.set_mode((PongGlobalVariables.width, PongGlobalVariables.height))

        # Initialize font.
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
