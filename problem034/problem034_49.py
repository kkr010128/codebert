class Dice:
    def __init__(self):
        self.front = '1'
        self.back = '6'
        self.top = '5'
        self.bottom = '2'
        self. right = '3'
        self.left = '4'
    def turnRight(self):
        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
        return self.top
    def turnLeft(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp
        return self.top
    def turnFront(self):
        temp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = temp
        return self.top
    def turnBack(self):
        temp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = temp
        return self.top

mydice = Dice()
mydice.top, mydice.front, mydice.right, mydice.left, mydice.back, mydice.bottom = input().split()

n = int(input())
for q in range(n):
    top, front = input().split()

    for rotate in range(3):
        mydice.turnFront()
        if mydice.top == front:
            break
        mydice.turnRight()
        if mydice.top == front:
            break
    mydice.turnFront()
    while top != mydice.top:
        mydice.turnRight()
    print(mydice.right)