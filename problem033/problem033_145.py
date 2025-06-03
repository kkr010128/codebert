# -*- coding: utf-8 -*-

class dice_class:
    def __init__(self, list):
        self.num = list

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
        self.num = [self.num[3], self.num[1], self.num[0], self.num[5], self.num[4], self.num[2]]

    def rollN(self):
        self.num = [self.num[1], self.num[5], self.num[2], self.num[3], self.num[0], self.num[4]]

    def rollS(self):
        self.num = [self.num[4], self.num[0], self.num[2], self.num[3], self.num[5], self.num[1]]

    def rollW(self):
        self.num = [self.num[2], self.num[1], self.num[5], self.num[0], self.num[4], self.num[3]]


if __name__ == "__main__":
    dice = dice_class(map(int, raw_input().split()))
    s = str(raw_input())
    dice.roll(s)
    print dice.num[0]