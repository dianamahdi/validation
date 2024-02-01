from SoupLanguage import SoupConfiguration


class HanoiTowersConfig(SoupConfiguration):
    def __init__(self, num_disks):
        self.towers = [list(range(num_disks, 0, -1)), [], []]

    def __hash__(self):
        return 42

    def __eq__(self, other):
        return self.towers == other.towers

    def __str__(self):
        return "Towers: " + str(self.towers)

    def can_move(self, source, destination):
        # Check if it's valid to move a disk from the source tower to the destination tower.
        source_tower = self.towers[source]
        destination_tower = self.towers[destination]

        if not source_tower:
            return False

        if not destination_tower or source_tower[-1] < destination_tower[-1]:
            return True

        return False

    def move_disk(self, source, destination):
        self.towers[destination].append(self.towers[source].pop())
        return self

    def is_final(self):
        if len(self.towers[0]) == 0 and len(self.towers[1]) == 0 and all(
                self.towers[2][i] > self.towers[2][i + 1] for i in range(len(self.towers[2]) - 1)):
            return True
        return False


def move_disk_and_check(config, source, destination):
    if config.can_move(source, destination):
        return config.move_disk(source, destination)
    return config


def main():
    num_disks = 3
    hanoi_config = HanoiTowersConfig(num_disks)

    print("Initial Configuration:")
    print(hanoi_config)

    source_tower = 0
    destination_tower = 2

    hanoi_config = move_disk_and_check(hanoi_config, source_tower, destination_tower)

    print("\nUpdated Configuration:")
    print(hanoi_config)

    if hanoi_config.is_final():
        print("\nCongratulations! You solved the Tower of Hanoi puzzle.")
    else:
        print("\nThe puzzle is not yet solved. Keep moving disks!")


if __name__ == '__main__':
    main()
