import copy
class Dice2:
    def __init__(self, nums):
        self.nums = nums
        self.dic = \
                {(1,2):3, (1,3):5, (1,4):2, (1,5):4, (2,3):1, (2,4):6, (2,6):3, (3,5):1, (3,6):5, (4,5):6, (4,6):2, (5,6):4}
    def output_right(self, x):
        x[0] = self.nums.index(x[0]) + 1
        x[1] = self.nums.index(x[1]) + 1
        nums = self.nums
        y = copy.deepcopy(x)
        x.sort()
        key = tuple(x)
        if tuple(y)==key:
            return nums[self.dic[key]-1]
        else:
            return nums[6-self.dic[key]]

dice = Dice2(list(map(int, input().split())))
q = int(input())
for i in range(q):
    print(dice.output_right(list(map(int, input().split()))))