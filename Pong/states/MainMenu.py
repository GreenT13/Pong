from framework.states.AbstractState import AbstractState


class MainMenu(AbstractState):
    def update(self, delta):
        print("Updating!")

    def draw(self, interpolation):
        print("Drawing!")

    def handleEvent(self, event):
        pass

    def actionAfterEvent(self):
        pass
