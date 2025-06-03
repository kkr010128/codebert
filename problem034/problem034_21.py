#coding:utf-8
#1_11_B 2015.4.20
class Dice:
    def __init__(self,ary):
        self.top = ary[0]
        self.south = ary[1]
        self.east = ary[2]
        self.west = ary[3]
        self.north = ary[4]
        self.bottom = ary[5]

    def roll_n(self):
        self.top , self.south , self.bottom , self.north = self.south , self.bottom , self.north , self.top

    def roll_e(self):
        self.top , self.west , self.bottom , self.east = self.west , self.bottom , self.east , self.top

    def roll(self):
        self.north , self.west , self.south , self.east = self.east , self.north , self.west , self.south

dice = Dice(input().split())
for i in range(int(input())):
    top,south = input().split()
    while dice.top != top or dice.south != south:
        dice.roll_n()
        if dice.top == top:
            while dice.south != south:
                dice.roll()
        elif dice.south == south:
            while dice.top != top:
                dice.roll_e()
    print(dice.east)