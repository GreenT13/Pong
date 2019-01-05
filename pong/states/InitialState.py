import pygame
from framework.states.AbstractState import AbstractState
from framework.states.Transition import Transition, TransitionConstants
from pong import PongGlobalVariables


class InitialState(AbstractState):
    def __init__(self):
        super().__init__()

        # Initialize screen.
        PongGlobalVariables.screen = pygame.display.set_mode((PongGlobalVariables.width, PongGlobalVariables.height))

        # Initialize font.
        pygame.font.init()

        # The first 'real' state to go to.
        self.nextTransition = Transition(TransitionConstants.MAIN_MENU, False)
