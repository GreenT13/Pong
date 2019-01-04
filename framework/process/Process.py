import pygame
from framework.process.GameClock import GameClock


class Process:
    """
    Framework class that will call the right functions at the right times.
        - ``update(delta)``: this function will be called each update interval. The delta parameter is the time passed (in seconds) before the previous call).
        - ``draw(interpolation)``: this function will be called for each update interval or when draw-cost is small enough.
        - ``handleEvent(event)``: this function will be called for each event that is recieved (also the quit event).
        - ``actionAfterEvent()``: this function will be called after all events are processed.
    """

    def __init__(self, state):
        """ See class description for more information. """
        self.clock = GameClock(update_callback=state.update, frame_callback=state.draw)
        self.handleEvent = state.handleEvent
        self.actionAfterEvent = state.actionAfterEvent

        # Store the state for later reference.
        self.state = state

    def startProcess(self):
        """ Starts the game. See class description. """
        running = True
        while running:
            # Execute all needed functions.
            self.clock.tick()

            # Handle all incoming events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Let the user handle the quiting.
                    self.handleEvent(event)

                    # When quiting, we always quit the loop.
                    running = False
                    break
                else:
                    self.handleEvent(event)

            # Any other actions may be executed.
            if self.actionAfterEvent:
                self.actionAfterEvent()

    def pause(self):
        pass

    def resume(self):
        pass
