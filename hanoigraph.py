from collections import deque


class HanoiConfig:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.start_state = (tuple(range(num_disks, 0, -1)), (), ())
        self.end_state = ((), (), tuple(range(num_disks, 0, -1)))


class HanoiRootedGraph(HanoiConfig):
    def __init__(self, num_disks):
        super().__init__(num_disks)

    def get_neighbors(self, state):
        neighbors = []
        for i, start_tower in enumerate(state):
            if start_tower:
                for j, end_tower in enumerate(state):
                    if i != j and (not end_tower or start_tower[-1] < end_tower[-1]):
                        new_state = list(map(list, state))
                        disk = new_state[i].pop()
                        new_state[j].append(disk)
                        neighbors.append(tuple(map(tuple, new_state)))
        return neighbors

    def bfs(self):
        visited = set()
        queue = deque([(self.start_state, [])])

        while queue:
            current_state, path = queue.popleft()
            if current_state == self.end_state:
                return path + [current_state]

            visited.add(current_state)
            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_state]))
        return None


# Example usage:
num_disks = 3
hanoi = HanoiRootedGraph(num_disks)
solution = hanoi.bfs()
if solution:
    print(f"Found solution in {len(solution) - 1} moves:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
