# bfs_function.py
from collections import deque


def bfs(rg, query):
    visited = set()
    queue = deque([(rg.start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if query(current_state):
            return path + [current_state]

        config_tuple = tuple(map(tuple, current_state))
        if config_tuple not in visited:
            visited.add(config_tuple)
            for neighbor in rg.get_neighbors(current_state):
                neighbor_tuple = tuple(map(tuple, neighbor))
                if neighbor_tuple not in visited:
                    queue.append((neighbor, path + [current_state]))
    return None
