# -*- coding: utf-8 -*-

class dice_class:
    def __init__(self, list):
        self.num = list

    def sut(self, top):  #set_up_top
        while True:
            if self.num[0] == top:
                break
            else:
                self.roll('E')
            if self.num[0] == top:
                break
            else:
                self.roll('N')

    def suf(self, front):   #set_up_front
        while True:
            if self.num[1] == front:
                break
            else:
                self.roll('SEN')

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
    n = int(raw_input())
    for i in range(n):
        top, front = map(int, raw_input().split())
        dice.sut(top)
        dice.suf(front)
        print dice.num[2]