from collections import deque


def bfs(rg, query):
    visited = set()
    queue = deque()
    i = True

    while i or len(queue) > 0:
        if i:
            neighbors = rg.roots()
            i = False
        else:
            current = queue.popleft()
            neighbors = rg.neighbors(current)
        for neighbor in neighbors:
            if query(neighbor):
                return neighbor, visited
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return None, visited




