class Dice:
    def __init__(self, d1, d2, d3, d4, d5, d6):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
    def S(self):
        tmp = self.d1
        self.d1 = self.d5
        self.d5 = self.d6
        self.d6 = self.d2
        self.d2 = tmp
    def N(self):
        tmp = self.d1
        self.d1 = self.d2
        self.d2 = self.d6
        self.d6 = self.d5
        self.d5 = tmp
    def E(self):
        tmp = self.d1
        self.d1 = self.d4
        self.d4 = self.d6
        self.d6 = self.d3
        self.d3 = tmp
    def W(self):
        tmp = self.d1
        self.d1 = self.d3
        self.d3 = self.d6
        self.d6 = self.d4
        self.d4 = tmp
    def output(self):
        print(self.d1)

d1, d2, d3, d4, d5, d6 = map(int, input().split())
dice = Dice(d1, d2, d3, d4, d5, d6)
M = input()
for i in range(len(M)):
    if M[i] == 'S':
        dice.S()
    elif M[i] == 'N':
        dice.N()
    elif M[i] == 'E':
        dice.E()
    elif M[i] == 'W':
        dice.W()
dice.output()
