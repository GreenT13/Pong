from framework.states.ProcessManager import ProcessManager
from framework.states.Transition import Transition, TransitionConstants

# The starting process
processManager = ProcessManager()
transition = Transition(TransitionConstants.INITIAL_STATE, False)

# Initialize things.
processManager.run(transition)
