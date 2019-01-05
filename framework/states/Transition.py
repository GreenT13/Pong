from enum import Enum, auto


class TransitionConstants(Enum):
    # Transitions that are representing specific actions.
    EXIT = auto()
    PREVIOUSLY_SAVED = auto()

    # Special state that must be present.
    INITIAL_STATE = auto()

    # Transitions linked to states.
    MAIN_MENU = auto()
    MAIN_MENU_OPTIONS = auto()
    GAME = auto()
    GAME_END = auto()
    PAUSE = auto()


class Transition:
    def __init__(self, transitionConstant, keepPrevious):
        self.transitionConstant = transitionConstant
        self.keepPrevious = keepPrevious


transitionStateMap = {
    # Special state that must be present.
    TransitionConstants.INITIAL_STATE: "pong.states.InitialState",

    # Game specific states.
    TransitionConstants.MAIN_MENU: "pong.states.MainMenu"
}
