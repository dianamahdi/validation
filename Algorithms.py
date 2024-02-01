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


def find_cycle(graph, initial, end):
    visited = []
    queue = deque()
    init = True
    while len(queue) != 0 or init:
        if init:
            voisin = initial
            init = False
        else:
            node = queue.popleft()
            voisin = graph.next(node)
        for n in voisin:
            if n not in visited:
                if n == end:
                    return True
                queue.append(n)
                visited.append(n)
    return False


def bfs2(rg, query):
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

        # Vérification que neighbors n'est pas None
        if neighbors is not None:
            for neighbor in neighbors:
                if query(neighbor):
                    return neighbor, visited
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return None, visited





