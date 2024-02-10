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
            voisin = graph.neighbors(node)  # Modify this line
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
            neighbors = rg.neighbors(current)  # Modify this line

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            if rg.is_accepting(neighbor):
                return False

            queue.append(neighbor)
            visited.add(neighbor)

    return True


def accepting_cycle(rg, query):
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
                return True
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return False


def accepting_predicate(rg, query):
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
                return True
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return False


# Test un Graph SAFE et un Graph NOT SAFE
class GraphWithAcceptingState:
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
        return 'A'

    def roots(self):
        return ['A']

    def neighbors(self, node):
        return self.graph.get(node, [])

    def is_accepting(self, node):
        return node == 'F'


class GraphWithoutAcceptingState:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': [],
            'D': [],
            'E': [],
            'F': []
        }

    def initial(self):
        return 'A'

    def roots(self):
        return ['A']

    def neighbors(self, node):
        return self.graph.get(node, [])

    def is_accepting(self, node):
        return node == 'F'


if __name__ == '__main__':
    graph_with_accepting_state = GraphWithAcceptingState()  # Safety = NO
    graph_without_accepting_state = GraphWithoutAcceptingState()  # Safety = YES

    # Test BFS function
    print("Testing BFS with accepting cycle:")
    result1, visited_nodes1 = bfs(graph_with_accepting_state, lambda x: x == 'F')
    print("Result:", result1)
    print("Visited Nodes:", visited_nodes1)
    print("------------------------")

    print("Testing BFS without accepting state:")
    result2, visited_nodes2 = bfs(graph_without_accepting_state, lambda x: x == 'F')
    print("Result:", result2)
    print("Visited Nodes:", visited_nodes2)
    print("------------------------")

    # Test bfs_safe function
    print("Testing bfs_safe with accepting state:")
    is_safe1 = bfs_safe(graph_with_accepting_state)
    print("Is Safe:", is_safe1)
    print("------------------------")

    print("Testing bfs_safe without accepting state:")
    is_safe2 = bfs_safe(graph_without_accepting_state)
    print("Is Safe:", is_safe2)
    print("------------------------")

    # Test accepting_cycle function
    print("Testing accepting_cycle with accepting state:")
    has_accepting_cycle1 = accepting_cycle(graph_with_accepting_state, lambda x: x == 'F')
    print("Has Accepting Cycle:", has_accepting_cycle1)
    print("------------------------")

    print("Testing accepting_cycle without accepting state:")
    has_accepting_cycle2 = accepting_cycle(graph_without_accepting_state, lambda x: x == 'F')
    print("Has Accepting Cycle:", has_accepting_cycle2)
    print("------------------------")

    # Test accepting_predicate function
    print("Testing accepting_predicate without accepting state:")
    has_accepting_predicate2 = accepting_predicate(graph_without_accepting_state, lambda x: x == 'E')
    print("Has Accepting Predicate:", has_accepting_predicate2)
    print("------------------------")



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





