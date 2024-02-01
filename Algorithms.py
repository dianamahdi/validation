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

def bfs_safe(rg):
    visited = set()
    queue = deque()
    start = True

    while start or len(queue) > 0:
        if start:
            neighbors = [rg.initial()]
            start = False
        else:
            current = queue.popleft()
            neighbors = rg.next(current)

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            if rg.is_accepting(neighbor):
                return False

            queue.append(neighbor)
            visited.add(neighbor)

    return True


#Test
class Graph:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

    def initial(self):
        return 'A'  # Change the initial node as needed

    def roots(self):
        return ['A']

    def neighbors(self, node):
        return self.graph.get(node, [])

    def is_accepting(self, node):
        return node == 'F'

if __name__ == '__main__':
    graph = Graph()

    # Test BFS function
    print("Testing BFS:")
    result, visited_nodes = bfs(graph, lambda x: x == 'F')
    print("Result:", result)
    print("Visited Nodes:", visited_nodes)
    print()

    # Test bfs_safe function
    print("Testing bfs_safe:")
    is_safe = bfs_safe(graph)
    print("Is Safe:", is_safe)


'''
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
'''




