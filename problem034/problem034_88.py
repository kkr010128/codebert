class Dice():
    def __init__(self):
        self.nums = list(range(6))
        self.work = list(range(6))

    def set_nums(self, n0, n1, n2, n3, n4, n5):
        self.nums[0] = n0
        self.nums[1] = n1
        self.nums[2] = n2
        self.nums[3] = n3
        self.nums[4] = n4
        self.nums[5] = n5

    def rotate(self, cmd):
        for i in range(6):
            # deepcopy
            self.work[i] = self.nums[i]

        if cmd == 'N':
            self.set_nums(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif cmd == 'S':
            self.set_nums(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1]),
        elif cmd == 'E':
            self.set_nums(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        else:
            self.set_nums(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])

    def top(self):
        return self.nums[0]

    def right(self, top, front):
        # サイコロの面IDを返す
        if top == 1:
            return [3,5,2,4][front-2]
        elif top == 6:
            return [4,2,5,3][front-2]
        elif top == 2:
            # 0が返る場合は不正なサイコロ
            return [4,0,1,6,0,3][front-1]
        elif top == 5:
            # 0が返る場合は不正なサイコロ
            return [3,0,6,1,0,4][front-1]
        elif top == 3:
            # 0が返る場合は不正なサイコロ
            return [2,6,0,0,1,5][front-1]
        elif top == 4:
            # 0が返る場合は不正なサイコロ
            return [5,1,0,0,6,2][front-1]
        else:
            pass

nums = [int(arg) for arg in input().split()]
d = Dice()
d.set_nums(*nums)
for _ in range(int(input())):
    top, front = [int(arg) for arg in input().split()]
    right_id = d.right(nums.index(top)+1, nums.index(front)+1)
    print(nums[right_id-1])

