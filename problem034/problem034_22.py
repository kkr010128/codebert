#!/usr/bin/env python

import random

class Dice:
    def __init__(self, top, s, e, w, n, bottom):
        self.top    = top
        self.s      = s
        self.e      = e
        self.w      = w
        self.n      = n
        self.bottom = bottom

    def rotate(self, dist):
        if dist == 'N':
            self.top, self.s, self.n, self.bottom = self.s, self.bottom, self.top, self.n 
        elif dist == 'S':
            self.s, self.bottom, self.top, self.n = self.top, self.s, self.n, self.bottom 
        elif dist == 'E':
            self.top, self.e, self.w, self.bottom = self.w, self.top, self.bottom, self.e 
        elif dist == 'W':
            self.w, self.top, self.bottom, self.e = self.top, self.e, self.w, self.bottom 

if __name__ == '__main__':
    dice = Dice(*map(int, raw_input().split()))

    ref = dict()
    while len(ref)<24:
        ref[(dice.top, dice.s)] = dice.e
        dice.rotate('NSEW'[random.randint(0,3)])

    for _ in range(input()):
        top, s = map(int, raw_input().split())
        print ref[(top, s)]

