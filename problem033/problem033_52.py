#!/usr/bin/env python3
# coding: utf-8

class Dice() :

    mask = {'N':(1,5,2,3,0,4), 'E':(3,1,0,5,4,2),
            'W':(2,1,5,0,4,3), 'S':(4,0,2,3,5,1)}

    def __init__(self, data):
        self.label = data

    def move(self, data):
        self.label = [self.label[idx] for idx in self.mask[data]]

    def get_up(self):
        return self.label[0]

dicedata = input().split()
orderdata = input()

newdice = Dice(dicedata)

[newdice.move(orderdata[idx]) for idx in range(0, len(orderdata))]

print(newdice.get_up())

