import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

def float_to_str(num):
    return str("{:.10f}".format(num))

def list_input(tp):
    return map(tp, str_input().split())

# # # # # # # # # # # # # # # # # # # # # # # # #

class Dice:
    pip = [0 for i in xrange(6)]

    def __init__(self, arg):
        self.pip = arg

    def rollDir(self, dr):
        nextPip = [0 for i in xrange(6)]
        if dr == "N":
            nextPip[0] = self.pip[1]
            nextPip[1] = self.pip[5]
            nextPip[2] = self.pip[2]
            nextPip[3] = self.pip[3]
            nextPip[4] = self.pip[0]
            nextPip[5] = self.pip[4]
        elif dr == "E":
            nextPip[0] = self.pip[3]
            nextPip[1] = self.pip[1]
            nextPip[2] = self.pip[0]
            nextPip[3] = self.pip[5]
            nextPip[4] = self.pip[4]
            nextPip[5] = self.pip[2]
        self.pip = nextPip

    def roll(self, dr):
        if dr == "N" or dr == "E":
            self.rollDir(dr)
        elif dr == "S":
            self.rollDir("N")
            self.rollDir("N")
            self.rollDir("N")
        elif dr == "W":
            self.rollDir("E")
            self.rollDir("E")
            self.rollDir("E")

dice = Dice(list_input(int))

for i in xrange(input()):
    a, b = list_input(int)

    while dice.pip[0] != a:
        if dice.pip[2] != a and dice.pip[3] != a:
            dice.roll("N")
        else:
            dice.roll("N")
            dice.roll("W")
            dice.roll("S")

    while dice.pip[1] != b:
        dice.roll("N")
        dice.roll("W")
        dice.roll("S")

    print dice.pip[2]