"""
  1
4 2 3 5
  6
  
"""

class Dice:
    def __init__(self, top, front, right, left, rear, bottom):
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.rear = rear
        self.bottom = bottom

    def N(self):
        self.tmp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.rear
        self.rear = self.tmp

    def E(self):
        self.tmp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = self.tmp

    def S(self):
        self.tmp = self.top
        self.top = self.rear
        self.rear = self.bottom
        self.bottom = self.front
        self.front = self.tmp

    def W(self):
        self.tmp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = self.tmp

    def show_numbers(self):
        print("上：%d"% self.top)
        print("前：%d"% self.front)
        print("右：%d"% self.right)
        print("左：%d"% self.left)
        print("後：%d"% self.rear)
        print("底：%d"% self.bottom)

    def show_top(self):
        print("%d" % self.top)


# ここからプログラム
buf = input().split(" ")
dice1 = Dice(int(buf[0]), int(buf[1]), int(buf[2]), int(buf[3]), int(buf[4]), int(buf[5]))

buf = input()
for ch in buf:
    if ch == "N":
        dice1.N()
    elif ch == "E":
        dice1.E()
    elif ch == "S":
        dice1.S()
    elif ch == "W":
        dice1.W()

dice1.show_top()

