class Dice:
    def __init__(self):
        self.d = list(map(int, input().split()))

    def setNum(self, n0, n1, n2, n3, n4, n5):
        self.d[0], self.d[1], self.d[2], self.d[3], self.d[4], self.d[5] = (
            n0,
            n1,
            n2,
            n3,
            n4,
            n5,
        )

    def roll(self, direction):
        if direction == "E":
            self.setNum(
                self.d[3], self.d[1], self.d[0], self.d[5], self.d[4], self.d[2]
            )
        elif direction == "N":
            self.setNum(
                self.d[1], self.d[5], self.d[2], self.d[3], self.d[0], self.d[4]
            )
        elif direction == "S":
            self.setNum(
                self.d[4], self.d[0], self.d[2], self.d[3], self.d[5], self.d[1]
            )
        elif direction == "W":
            self.setNum(
                self.d[2], self.d[1], self.d[5], self.d[0], self.d[4], self.d[3]
            )

    def top(self):
        return self.d[0]

    def setTop(self, t):
        if self.d[0] == t:
            return
        elif self.d[1] == t:
            self.roll("N")
        elif self.d[2] == t:
            self.roll("W")
        elif self.d[3] == t:
            self.roll("E")
        elif self.d[4] == t:
            self.roll("S")
        elif self.d[5] == t:
            self.roll("N")
            self.roll("N")

    def getRight(self, f):
        if self.d[2] == f:
            return self.d[4]
        elif self.d[3] == f:
            return self.d[1]
        elif self.d[4] == f:
            return self.d[3]
        else:
            return self.d[2]


dice = Dice()
q = int(input())
for i in range(q):
    t, f = map(int, input().split())
    dice.setTop(t)
    print(dice.getRight(f))

