capacity = (12, 8, 5)  # Maximum capacities of 3 jugs -> x, y, z
x = capacity[0]  # Capacity of jug A
y = capacity[1]  # Capacity of jug B
z = capacity[2]  # Capacity of jug C

# to mark visited states
memory = {}
# store solution path
ans = []

def get_all_states(state):
    # Let the 3 jugs be called a, b, c
    a = state[0]  # Current amount in jug A
    b = state[1]  # Current amount in jug B
    c = state[2]  # Current amount in jug C

    # Check if the goal state is reached
    if a == 6 and b == 6:
        ans.append(state)
        return True

    # if current state is already visited earlier
    if (a, b, c) in memory:
        return False
    
    # Mark the current state as visited
    memory[(a, b, c)] = 1

    # Empty jug A
    if a > 0:
        # Empty A into B
        if a + b <= y:
            if get_all_states((0, a + b, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                ans.append(state)
                return True
        
        # Empty A into C
        if a + c <= z:
            if get_all_states((0, b, a + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                ans.append(state)
                return True

    # Empty jug B
    if b > 0:
        # Empty B into A
        if a + b <= x:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                ans.append(state)
                return True

        # Empty B into C
        if b + c <= z:
            if get_all_states((a, 0, b + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                ans.append(state)
                return True

    # Empty jug C
    if c > 0:
        # Empty C into A
        if a + c <= x:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                ans.append(state)
                return True

        # Empty C into B
        if b + c <= y:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                ans.append(state)
                return True

    return False

# Initial state: jug A is full, jugs B and C are empty
initial_state = (12, 0, 0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()  # Reverse to get the path from the start to the goal
for i in ans:
    print(i)
