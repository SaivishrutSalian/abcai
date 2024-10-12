from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            # Put space before A because a string can also consider spaces with the letters.
            # E.g., "HELLO WORLD" has a space between the two words.
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        wrong = sum([1 if state[i] != GOAL[i] else 0 for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

# Do not put a space between single quotes for the initial state.
problem = HelloProblem(initial_state='')

result = astar(problem)
print(result.state)
print(result.path())
