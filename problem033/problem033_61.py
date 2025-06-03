class Dice(object):

    def __init__(self, num):
        self.num = num

    def rotate_S(self):
        self.num = [self.num[4], self.num[0], self.num[2], self.num[3], self.num[5], self.num[1]]

    def rotate_N(self):
        self.num = [self.num[1], self.num[5], self.num[2], self.num[3], self.num[0], self.num[4]]

    def rotate_W(self):
        self.num = [self.num[2], self.num[1], self.num[5], self.num[0], self.num[4], self.num[3]]

    def rotate_E(self):
        self.num = [self.num[3], self.num[1], self.num[0], self.num[5], self.num[4], self.num[2]]


dice = Dice(map(int, raw_input().split()))
order = raw_input()
for i in range(len(order)):
    if order[i] == 'S':
        dice.rotate_S()
    elif order[i] == 'N':
        dice.rotate_N()
    elif order[i] == 'W':
        dice.rotate_W()
    elif order[i] == 'E':
        dice.rotate_E()

print dice.num[0]