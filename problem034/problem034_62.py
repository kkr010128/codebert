class Dice(object):
    def __init__(self, nums):
        self.top, self.front, self.right, self.left, self.back, self.bottom = nums

    def roll(self, directions):
        if directions == 'E':
            self.top, self.right, self.left, self.bottom = self.left, self.top, self.bottom, self.right
            return

        if directions == 'N':
            self.top, self.front, self.back, self.bottom = self.front, self.bottom, self.top, self.back
            return

        if directions == 'S':
            self.top, self.front, self.back, self.bottom = self.back, self.top, self.bottom, self.front
            return

        if directions == 'W':
            self.top, self.right, self.left, self.bottom = self.right, self.bottom, self.top, self.left
            return

        self.roll(directions[0])
        self.roll(directions[1:])

if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    d = Dice(nums)
    q = int(input())
    for i in range(q):
        top, front = [int(x) for x in input().split()]

        if(top == d.front):
            d.roll('N')
        elif(top == d.right):
            d.roll('W')
        elif(top == d.left):
            d.roll('E')
        elif(top == d.back):
            d.roll('S')
        elif(top == d.bottom):
            d.roll('NN')

        if(front == d.right):
            d.roll('WSE')
        elif(front == d.left):
            d.roll('ESW')
        elif(front == d.back):
            d.roll('SENWSE')

        print(d.right)