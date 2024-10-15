from collections import deque

def water_jug():
    
    # initial state -> ( jug A, jug B, jug C)
    initial_state = (12, 0, 0)
    goal = 6
    queue = deque([initial_state])
    visited = []
    path = []


    while queue:
        state = queue.popleft()
        a, b, c = state
        
        if a == goal or b == goal or c == goal:
            path.append(state)
            return path

        if state in visited:
            continue


        visited.append(state)
        path.append(state)


        # from A -> B
        if a > 0 and b < 8:
            transfer = min(a, 8-b)
            queue.append((a - transfer, b+transfer, c))

        # from A -> C
        if a > 0 and b < 5:
            transfer = min(a, 5 - c)
            queue.append((a - transfer, b, c + transfer))

        # from B -> A
        if b > 0 and a < 12:
            transfer = min(b, 12 - a)
            queue.append((a + transfer, b - transfer, c))

        # from B -> C
        if b > 0 and c < 5:
            transfer = min(b, 5 - c)
            queue.append((a, b - transfer, c + transfer))

        # from C -> A
        if c > 0 and a < 12:
            transfer = min(c, 12 - a)
            queue.append((a + transfer, b, c - transfer))

        # from C -> B
        if c > 0 and b < 8:
            transfer = min(c, 8 - b)
            queue.append((a, c - transfer, b + transfer))

    return None

result = water_jug()

if result:
    for i in result:
        print(i)
else:
    print("no solution found")

