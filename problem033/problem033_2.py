class Dice:
    __slots__ = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6']

    def __init__(self, n_tup):

        self.n1 = n_tup[0]
        self.n2 = n_tup[1]
        self.n3 = n_tup[2]
        self.n4 = n_tup[3]
        self.n5 = n_tup[4]
        self.n6 = n_tup[5]

    def roll(self, direction):
        if direction == "N":
            self.n1, self.n2, self.n6, self.n5 \
                = self.n2, self.n6, self.n5, self.n1
        elif direction == "E":
            self.n1, self.n3, self.n6, self.n4 \
                = self.n4, self.n1, self.n3, self.n6
        if direction == "S":
            self.n1, self.n2, self.n6, self.n5 \
                = self.n5, self.n1, self.n2, self.n6
        if direction == "W":
            self.n1, self.n3, self.n6, self.n4 \
                = self.n3, self.n6, self.n4, self.n1

dice = Dice([int(x) for x in input().split()])

cmd = input()
for i in range(len(cmd)):
    dice.roll(cmd[i])

print(dice.n1)