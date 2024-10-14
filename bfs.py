def bfs(graph, start_node):
    queue = deque([start_node])
    visited = {start_node}

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')

