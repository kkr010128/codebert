class Dice():
    def __init__(self, nums):
        self.nums = nums
        self.top, self.front, self.right = 0, 1, 2

    def move(self, op):
        for c in op:
            if c == 'N':
                self.top, self.front = self.front, 5 - self.top
            elif c == 'S':
                self.top, self.front = 5 - self.front, self.top
            elif c == 'E':
                self.top, self.right = 5 - self.right, self.top
            else:
                self.top, self.right = self.right, 5 - self.top

dice = Dice([int(n) for n in input().split()])
dice.move(input())
print(dice.nums[dice.top])