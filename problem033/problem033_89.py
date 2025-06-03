class Dice:
    """????????????????????????"""
    def __init__(self, s):
        self.s1 = s[0]
        self.s2 = s[1]
        self.s3 = s[2]
        self.s4 = s[3]
        self.s5 = s[4]
        self.s6 = s[5]

    def roll(self, direction):          # ???????????????????§??????¢????????¢
        temp = self.s1
        if direction == "E":
            self.s1 = self.s4
            self.s4 = self.s6
            self.s6 = self.s3
            self.s3 = temp
        elif direction == "N":
            self.s1 = self.s2
            self.s2 = self.s6
            self.s6 = self.s5
            self.s5 = temp
        elif direction == "S":
            self.s1 = self.s5
            self.s5 = self.s6
            self.s6 = self.s2
            self.s2 = temp
        elif direction == "W":
            self.s1 = self.s3
            self.s3 = self.s6
            self.s6 = self.s4
            self.s4 = temp

s = list(map(int, input().split()))
dice1 = Dice(s)
command = input()

for i in range(len(command)):
    dice1.roll(command[i])

print(dice1.s1)