class Dice:
    def __init__(self,u,s,e,w,n,d):
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.u = u
        self.d = d
    def roll(self,dir):
        if (dir == "N"):
            tmp = self.n
            self.n = self.u
            self.u = self.s
            self.s = self.d
            self.d = tmp
        elif (dir == "E"):
            tmp = self.e
            self.e = self.u
            self.u = self.w
            self.w = self.d
            self.d = tmp
        elif (dir == "S"):
            tmp = self.s
            self.s = self.u
            self.u = self.n
            self.n = self.d
            self.d = tmp
        elif (dir == "W"):
            tmp = self.w
            self.w = self.u
            self.u = self.e
            self.e = self.d
            self.d = tmp

spots = raw_input().split()
operations = raw_input()

dice = Dice(*spots)
for i in operations:
    dice.roll(i)

print dice.u