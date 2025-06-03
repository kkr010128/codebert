# -*- coding: utf-8 -*-


class Dice:
    def __init__(self, n):
        self.upper    = n[0]
        self.backward = n[1]
        self.right    = n[2]
        self.left     = n[3]
        self.ahead    = n[4]
        self.bottom   = n[5]

    def roll_north(self):
        self.upper, self.ahead, self.bottom, self.backward = self.backward, self.upper, self.ahead, self.bottom

    def roll_south(self):
        self.upper, self.ahead, self.bottom, self.backward = self.ahead, self.bottom, self.backward, self.upper

    def roll_east(self):
        self.upper, self.right, self.bottom, self.left = self.left, self.upper, self.right, self.bottom

    def roll_west(self):
        self.upper, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.upper


dice_info = Dice(list(map(int, input().split())))
order = list(input())

for i in range(len(order)):
    if 'N' in order[i]:
        dice_info.roll_north()

    elif 'S' in order[i]:
        dice_info.roll_south()

    elif 'E' in order[i]:
        dice_info.roll_east()

    elif'W' in order[i]:
        dice_info.roll_west()

print(dice_info.upper)

