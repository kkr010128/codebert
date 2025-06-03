import random

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
for i in range(int(input())):
    up, front = map(int, input().split())

    while(True):
        direction = random.randint(0, 3)
        if direction == 0:
            dice.north()
        if direction == 1:
            dice.south()
        if direction == 2:
            dice.east()
        if direction == 3:
            dice.west()

        if dice.labels[0] == up and dice.labels[1] == front:
            print(dice.labels[2])
            break