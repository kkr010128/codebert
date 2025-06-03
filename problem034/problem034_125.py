nums = list(map(int, input().split()))

import random

class dice:
    def __init__(self):
        self.top = 0
        self.right = 0
        self.front = 0
        self.left = 0
        self.back = 0
        self.bottom = 0
    
    def set_num(self, nums):
        self.top, self.front, self.right, self.left, self.back, self.bottom = nums
        return self
    
    def get_right(self, f_top, f_front):
        while f_top!=self.top or f_front!=self.front:
            self.roll(random.randint(0,3))
        return self.right
        
    def roll(self, command):
        if command==0:
            self.top, self.front, self.right, self.left, self.back, self.bottom = self.left, self.front, self.top, self.bottom, self.back, self.right
        elif command==1:
            self.top, self.front, self.right, self.left, self.back, self.bottom = self.right, self.front, self.bottom, self.top, self.back, self.left
        elif command==2:
            self.top, self.front, self.right, self.left, self.back, self.bottom = self.front, self.bottom, self.right, self.left, self.top, self.back
        elif command==3:
            self.top, self.front, self.right, self.left, self.back, self.bottom = self.back, self.top, self.right, self.left, self.bottom, self.front
            

d = dice()
d.set_num(nums)

n = int(input())
for i in range(n):
    f_t, f_r = map(int, input().split())
    print(d.get_right(f_t, f_r))
