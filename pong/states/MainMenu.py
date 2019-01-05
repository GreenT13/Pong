import pygame

from framework.draw import DrawUtil
from framework.states.AbstractState import AbstractState
from framework.states.Transition import TransitionConstants
from pong import PongConstants, PongGlobalVariables


class MainMenu(AbstractState):
    def startGame(self):
        self.setNextTransition(TransitionConstants.GAME, False)

    def options(self):
        # self.setNextTransition(TransitionConstants.MAIN_MENU_OPTIONS, False)
        print("I don't really have options yet!")

    def exit(self):
        self.setNextTransition(TransitionConstants.EXIT, False)

    menuItems = [
        ['Start Game', startGame],
        ['Options', options],
        ['Exit', exit]
    ]

    def __init__(self):
        super().__init__()
        self.pressedKey = {}

        # Remember which item in the menu is selected.
        self.selectedIndex = 0

    def update(self, delta):
        pass

    def draw(self, interpolation):
        screen = PongGlobalVariables.screen

        # Clear the screen.
        screen.fill(0)

        # Draw menu items in the middle of the screen.
        # Loop over the list on index, because we need it for DrawUtil.determineMiddleOfMenuItem.
        for i in range(0, len(MainMenu.menuItems)):
            adjustedY = DrawUtil.determineMiddleOfMenuItem(len(MainMenu.menuItems),
                                                           5, PongConstants.FONT_SIZE, i)
            centerY = screen.get_rect().centery + adjustedY
            centerX = screen.get_rect().centerx
            DrawUtil.writeTextOnScreen(MainMenu.menuItems[i][0],
                                       centerX, centerY, underlineItem=(i == self.selectedIndex))

    def handleEvent(self, event):
        if pygame.QUIT == event.type:
            pygame.quit()
            self.setNextTransition(TransitionConstants.EXIT, False)

        # Check for key presses.
        if pygame.KEYDOWN == event.type:
            self.pressedKey[event.key] = True
        elif pygame.KEYUP == event.type:
            # Only register KEYUP if the key is still present.
            if event.key in self.pressedKey:
                self.pressedKey[event.key] = False

    def actionAfterEvent(self):
        # If a key is contained in the dictionary, it was pushed down.
        # If the value is False, the key was also released.

        # We cannot remove keys from the array during the for-loop, so we need to store them.
        removedKeys = []

        # Do all needed actions for keyDown or keyPressed.
        for key, isKeyDown in self.pressedKey.items():
            if isKeyDown:
                # We have no scrolling keys.
                pass

            if not isKeyDown:
                removedKeys.append(key)
                if pygame.K_UP == key:
                    # We lower the index, but not less than 0.
                    self.selectedIndex = max(self.selectedIndex - 1, 0)
                elif pygame.K_DOWN == key:
                    # We increase the index, but not more than the maximum.
                    self.selectedIndex = min(self.selectedIndex + 1, len(MainMenu.menuItems) - 1)
                elif pygame.K_RETURN == key or pygame.K_KP_ENTER == key:
                    # Execute the command
                    MainMenu.menuItems[self.selectedIndex][1](self)

        for key in removedKeys:
            self.pressedKey.pop(key)
