class Dice:
    def __init__(self, labels):
        self.labels = labels

    def north(self):
        self.change([2, 6, 3, 4, 1, 5])

    def south(self):
        self.change([5, 1, 3, 4, 6, 2])

    def east(self):
        self.change([4, 2, 1, 6, 5, 3])

    def west(self):
        self.change([3, 2, 6, 1, 5, 4])

    def change(self, convert):
        result = []
        for i in range(6):
            result.append(self.labels[convert[i] - 1])

        self.labels = result


dice = Dice(list(map(int, input().split())))
for direction in input():
    if direction == 'N':
        dice.north()
    if direction == 'S':
        dice.south()
    if direction == 'E':
        dice.east()
    if direction == 'W':
        dice.west()

print(dice.labels[0])