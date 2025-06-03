class Dice:
    top     = -1
    front   = -1
    right   = -1
    left    = -1
    back    = -1
    bottom  = -1
    
    def __init__(self, top, front, right, left, back, bottom):
        self.top, self.front, self.right, self.left, self.back, self.bottom = top, front, right, left, back, bottom
    
    def rolltoN(self):
        self.top, self.front, self.back, self.bottom = self.front, self.bottom, self.top, self.back
    
    def rolltoS(self):
        self.top, self.front, self.back, self.bottom = self.back, self.top, self.bottom, self.front
    
    def rolltoW(self):
        self.top, self.right, self.left, self.bottom = self.right, self.bottom, self.top, self.left
    
    def rolltoE(self):
        self.top, self.right, self.left, self.bottom = self.left, self.top, self.bottom, self.right
    
    def returntop(self):
        return self.top

a,b,c,d,e,f = map(int, input().split())
dice = Dice(a,b,c,d,e,f)
strorder = input()

for c in strorder:
    if c == 'N':
        dice.rolltoN()
    elif c == 'S':
        dice.rolltoS()
    elif c == 'W':
        dice.rolltoW()
    elif c == 'E':
        dice.rolltoE()
print(dice.returntop())
