from framework.states.Transition import Transition


class AbstractState:
    def __init__(self):
        self.nextTransition = None

    def getNextTransition(self):
        return self.nextTransition

    def update(self, delta):
        pass

    def draw(self, interpolation):
        pass

    def handleEvent(self, event):
        pass

    def actionAfterEvent(self):
        pass

    def setNextTransition(self, transitionConstant, keepPrevious):
        self.nextTransition = Transition(transitionConstant, keepPrevious)
