# coding:utf-8
class Dice:
    def __init__(self):
        self.f = [0 for i in range(6)]
    def roll_z(self): self.roll(1,2,4,3)
    def roll_y(self): self.roll(0,2,5,3)
    def roll_x(self): self.roll(0,1,5,4)
    def roll(self,i,j,k,l):
        t = self.f[i]; self.f[i] = self.f[j]; self.f[j] = self.f[k]; self.f[k] = self.f[l]; self.f[l] = t
    def move(self,ch):
        if ch == 'E':
            for i in range(3):
                self.roll_y()
        if ch == 'W':
            self.roll_y()
        if ch == 'N':
            self.roll_x()
        if ch == 'S':
            for i in range(3):
                self.roll_x()
dice = Dice()
dice.f = map(int, raw_input().split())
com = raw_input()
for i in range(len(com)):
    dice.move(com[i])
print dice.f[0]

