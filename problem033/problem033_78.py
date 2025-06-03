class Dice(object):

    def __init__(self, n):
        self.n = n
    def move(self, to):
        if to == 'N':
            self.n[0], self.n[1], self.n[4], self.n[5] = self.n[1], self.n[5], self.n[0], self.n[4]
        elif to == 'E':
            self.n[0], self.n[2], self.n[3], self.n[5] = self.n[3], self.n[0], self.n[5], self.n[2]
        elif to == 'S':
            self.n[0], self.n[1], self.n[4], self.n[5] = self.n[4], self.n[0], self.n[5], self.n[1]
        elif to == 'W':
            self.n[0], self.n[2], self.n[3], self.n[5] = self.n[2], self.n[5], self.n[0], self.n[3]
    def top(self):
        return self.n[0]

dice = Dice([int(i) for i in input().split()])
move = input()
for m in move:
    dice.move(m)
print(dice.top())

