# coding: utf-8

class Dice(object):
    def __init__(self, num_list):
        self.num = num_list

    def west(self):
        num = list(self.num)
        before = [5, 2, 0, 3]
        after = [2, 0, 3, 5]
        for i in range(4):
            self.num[after[i]] = num[before[i]]
        return self.num[5]

    def east(self):
        num = list(self.num)
        before = [5, 2, 0, 3]
        after = [3, 5, 2, 0]
        for i in range(4):
            self.num[after[i]] = num[before[i]]
        return self.num[5]

    def north(self):
        num = list(self.num)
        before = [0, 1, 5, 4]
        after = [4, 0, 1, 5]
        for i in range(4):
            self.num[after[i]] = num[before[i]]
        return self.num[5]

    def south(self):
        num = list(self.num)
        before = [0, 1, 5, 4]
        after = [1, 5, 4, 0]
        for i in range(4):
            self.num[after[i]] = num[before[i]]
        return self.num[5]

if __name__ == "__main__":
    num_list = [int(i) for i in raw_input().split()]
    dice = Dice(num_list)
    for order in raw_input():
        if order == "E": dice.east()
        elif order == "W": dice.west()
        elif order == "S": dice.south()
        elif order == "N": dice.north()
    print dice.num[0]