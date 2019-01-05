from framework.states.Transition import transitionStateMap, TransitionConstants, Transition
from framework.process.Process import Process
import importlib


class ProcessManager:
    def __init__(self):
        self.previousProcess = []

    def run(self, transition):
        usePreviouslySaved = False
        # While loop with condition at the end.
        while True:
            # Get the process to switch to.
            if usePreviouslySaved:
                process = self.previousProcess.pop()
            else:
                state = ProcessManager.instantiateClass(transitionStateMap.get(transition.transitionConstant))
                process = Process(state)

            # Run the process and get a transition.
            if usePreviouslySaved:
                transition = process.resume()

                # Reset the variable to default value.
                usePreviouslySaved = False
            else:
                transition = process.startProcess()

            # If transition is None, something went wrong. We show a warning, and initialize an EXIT transition.
            if transition is None:
                print('Warning: Transition is None. We quit the application.')
                transition = Transition(TransitionConstants.EXIT, False)

            # We need to save process if indicated.
            if transition.keepPrevious:
                self.previousProcess.append(process)
                process.pause()

            # In case of specific transitions, we do some specific actions.
            if TransitionConstants.EXIT == transition.transitionConstant:
                break
            elif TransitionConstants.PREVIOUSLY_SAVED == transition.transitionConstant:
                usePreviouslySaved = True

    @staticmethod
    def instantiateClass(moduleName):
        # We assume the class name is identical to the module name.
        className = moduleName.rsplit(".", 1)[1]
        myClass = getattr(importlib.import_module(moduleName), className)
        return myClass()
