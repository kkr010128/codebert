# -*- coding: utf-8 -*-

class dice_class:
    def __init__(self, top, front, right, left, back, bottom):
        self.top    =   top
        self.front  =   front
        self.right  =   right
        self.left   =   left
        self.back   =   back
        self.bottom =   bottom

    def roll(self, s):
        for i in s:
            if i == 'E':
                self.rollE()
            elif i == 'N':
                self.rollN()
            elif i == 'S':
                self.rollS()
            elif i == 'W':
                self.rollW()

    def rollE(self):
        tmp         =   self.top
        self.top    =   self.left
        self.left   =   self.bottom
        self.bottom =   self.right
        self.right  =   tmp

    def rollN(self):
        tmp         =   self.top
        self.top    =   self.front
        self.front  =   self.bottom
        self.bottom =   self.back
        self.back   =   tmp

    def rollS(self):
        tmp         =   self.top
        self.top    =   self.back
        self.back   =   self.bottom
        self.bottom =   self.front
        self.front  =   tmp

    def rollW(self):
        tmp         =   self.top
        self.top    =   self.right
        self.right  =   self.bottom
        self.bottom =   self.left
        self.left   =   tmp

if __name__ == "__main__":
    a = map(int, raw_input().split())
    s = str(raw_input())
    dice = dice_class(a[0], a[1], a[2], a[3], a[4], a[5])
    dice.roll(s)
    print dice.top