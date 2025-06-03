d = list(map(int, input().split()))
order = input()
class Dice():
    def __init__(self, d):
        self.dice = d

    def InsSN(self, one, two, five, six):
        self.dice[0] = one
        self.dice[1] = two
        self.dice[4] = five
        self.dice[5] = six
        
    def InsWE(self, one, three, four, six):
        self.dice[0] = one
        self.dice[2] = three
        self.dice[3] = four
        self.dice[5] = six

    def S(self):
        one = self.dice[4]
        two = self.dice[0]
        five = self.dice[5]
        six = self.dice[1]
        self.InsSN(one, two, five, six)

    def N(self):
        one = self.dice[1]
        two = self.dice[5]
        five = self.dice[0]
        six = self.dice[4]
        self.InsSN(one, two, five, six)
 
    def W(self):
        one = self.dice[2]
        three = self.dice[5]
        four = self.dice[0]
        six = self.dice[3]
        self.InsWE(one, three, four, six)
        
    def E(self):
        one = self.dice[3]
        three = self.dice[0]
        four = self.dice[5]
        six = self.dice[2]
        self.InsWE(one, three, four, six)
        
    def roll(self, order):
        if order == 'S':
            self.S()
        elif order == 'N':
            self.N()
        elif order == 'E':
            self.E()
        elif order == 'W':
            self.W()
d = Dice(d)
for o in order:
    d.roll(o)
print(d.dice[0])