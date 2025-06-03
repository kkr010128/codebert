class Dice(object):
    def __init__(self):
        self.number = [0 for _ in range(6)]
        self.before = [0 for _ in range(6)]

    def set_number(self, l):
        for i in range(6):
            self.number[i] = l[i]

    def roll(self, loc):
        d = {
            'N': (1, 5, 2, 3, 0, 4),
            'S': (4, 0, 2, 3, 5, 1),
            'E': (3, 1, 0, 5, 4, 2),
            'W': (2, 1, 5, 0, 4, 3)
        }
        for i in range(6):
            self.before[i] = self.number[i]

        for i, j in enumerate(d[loc]):
            self.number[i] = self.before[j]

    def get_Top(self):
        return self.number[0]


if __name__ == '__main__':
    l = list(map(int, input().split()))
    dice = Dice()
    dice.set_number(l)
    s = input()
    for i in s:
        dice.roll(i)
    print(dice.get_Top())
