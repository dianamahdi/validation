from collections import deque

class HanoiConfig:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        # Utilisation de listes au lieu de tuples pour représenter les tours
        self.start_state = [list(range(num_disks, 0, -1)), [], []]
        self.end_state = [[], [], list(range(num_disks, 0, -1))]

class HanoiRootedGraph(HanoiConfig):
    def __init__(self, num_disks):
        super().__init__(num_disks)

    def get_neighbors(self, config):
        neighbors = []
        for i, start_tower in enumerate(config):
            if start_tower:  # Check if there is at least one disk on the tower
                for j, end_tower in enumerate(config):
                    if i != j and (not end_tower or start_tower[-1] < end_tower[-1]):
                        # Effectuer une copie profonde pour créer un nouvel état
                        new_config = [tower[:] for tower in config]
                        disk = new_config[i].pop()  # Retirer le disque du sommet de la tour de départ
                        new_config[j].append(disk)  # Ajouter le disque au sommet de la tour d'arrivée
                        neighbors.append(new_config)
        return neighbors

    def bfs(self):
        visited = set()
        queue = deque([(self.start_state, [])])

        while queue:
            current_config, path = queue.popleft()
            if current_config == self.end_state:
                return path + [current_config]

            config_tuple = tuple(map(tuple, current_config))  # Convertir en tuple pour les sets
            if config_tuple not in visited:
                visited.add(config_tuple)
                for neighbor in self.get_neighbors(current_config):
                    neighbor_tuple = tuple(map(tuple, neighbor))  # Convertir en tuple pour les sets
                    if neighbor_tuple not in visited:
                        queue.append((neighbor, path + [current_config]))
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
