
class Dice:
    def __init__(self, label):
        self.d = label

    def roll(self, direction):
        if direction == "N":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[1], self.d[5], self.d[4], self.d[0]
        elif direction == "S":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[4], self.d[0], self.d[1], self.d[5]
        elif direction == "E":
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[3], self.d[0], self.d[2], self.d[5]
        else:
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[2], self.d[5], self.d[3], self.d[0]

label = [int(i) for i in input().split()]
cmd = input()

dice1 = Dice(label)

for i in cmd:
    dice1.roll(i)

print(dice1.d[0])