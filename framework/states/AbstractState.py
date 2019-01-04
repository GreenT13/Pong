class AbstractState:
    def __init__(self):
        self.f_update = self.update
        self.f_draw = self.draw
        self.f_handleEvent = self.handleEvent
        self.f_actionAfterEvent = self.actionAfterEvent
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
