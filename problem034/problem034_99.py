# -*- coding: utf-8 -*-
from sys import stdin

class Dice:

    def __init__(self,dicelist):
        self.dice_list = dicelist

    def roll(self, direction):
        work = list(self.dice_list)
        if (direction == 'N'):
            self.dice_list[0] = work[1]
            self.dice_list[1] = work[5]
            self.dice_list[2] = work[2]
            self.dice_list[3] = work[3]
            self.dice_list[4] = work[0]
            self.dice_list[5] = work[4]
        elif (direction == 'E'):
            self.dice_list[0] = work[3]
            self.dice_list[1] = work[1]
            self.dice_list[2] = work[0]
            self.dice_list[3] = work[5]
            self.dice_list[4] = work[4]
            self.dice_list[5] = work[2]
        elif (direction == 'S'):
            self.dice_list[0] = work[4]
            self.dice_list[1] = work[0]
            self.dice_list[2] = work[2]
            self.dice_list[3] = work[3]
            self.dice_list[4] = work[5]
            self.dice_list[5] = work[1]
        elif (direction == 'W'):
            self.dice_list[0] = work[2]
            self.dice_list[1] = work[1]
            self.dice_list[2] = work[5]
            self.dice_list[3] = work[0]
            self.dice_list[4] = work[4]
            self.dice_list[5] = work[3]

    def roll_until_index0top(self,num0):
        if self.dice_list[0] == num0:
            return
        commands = ['E', 'E', 'E', 'N', 'N', 'N']
        for c in commands:
            self.roll(c)
            if self.dice_list[0] == num0:
                return
        else:
            print('error')

    def get_index_by_number(self, num):
        for i in range(len((self.dice_list))):
            if self.dice_list[i] == num:
                return i
        else:
            return -1

    def get_index2_number(self, num1):
        index1 = self.get_index_by_number(num1)
        if index1 == 1:
            return self.dice_list[2]
        elif (index1 == 2):
            return self.dice_list[4]
        elif (index1 == 3):
            return self.dice_list[1]
        elif (index1 == 4):
            return self.dice_list[3]
        else:
            print('error 2')

    def getTop(self):
        return self.dice_list[0]


dice_list = list(map(int, stdin.readline().rstrip().split()))
q = int(stdin.readline().rstrip())
dice = Dice(dice_list)

for i in range(q):
    num0_num1 = list(map(int, stdin.readline().rstrip().split()))
    dice.roll_until_index0top(num0_num1[0])
    print(dice.get_index2_number(num0_num1[1]))
