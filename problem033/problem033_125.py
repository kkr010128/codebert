# coding: utf-8
# Your code here!

class dice(object):
    def __init__(self, arr):
        self.top = arr[0]
        self.side_s = arr[1]
        self.side_e = arr[2]
        self.side_w = arr[3]
        self.side_n = arr[4]
        self.bottom = arr[5]
    def roll(self, s):
        if s=='S':
            tmp = self.bottom
            self.bottom = self.side_s
            self.side_s = self.top
            self.top = self.side_n
            self.side_n = tmp
        elif s=='E':
            tmp = self.bottom
            self.bottom = self.side_e
            self.side_e = self.top
            self.top = self.side_w
            self.side_w = tmp
        elif s=='W':
            tmp = self.bottom
            self.bottom = self.side_w
            self.side_w = self.top
            self.top = self.side_e
            self.side_e = tmp
        elif s=='N':
            tmp = self.bottom
            self.bottom = self.side_n
            self.side_n = self.top
            self.top = self.side_s
            self.side_s = tmp
    

s = input().split()
# s = '1 2 4 8 16 32'.split()

dice = dice(s)
arr = input()
for a in arr:
    dice.roll(a)
# print(type(dice))
print(dice.top)

