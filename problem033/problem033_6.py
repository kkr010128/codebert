class Dice:
    def __init__(self, list):
        self.list = list  #listのinput
    def roll_n(self):
        self.list = [self.list[1], self.list[5], self.list[2], self.list[3], self.list[0], self.list[4]]
    def roll_s(self):
        self.list = [self.list[4], self.list[0], self.list[2], self.list[3], self.list[5], self.list[1]]
    def roll_e(self):
        self.list = [self.list[3], self.list[1], self.list[0], self.list[5], self.list[4], self.list[2]]
    def roll_w(self):
        self.list = [self.list[2], self.list[1], self.list[5], self.list[0], self.list[4], self.list[3]]
    def print0(self):
        print(self.list[0])


list = list(map(int, input().split()))
direct = input()
instance = Dice(list)
for i in direct:
    if i == 'N':
        instance.roll_n()
    if i == 'S':
        instance.roll_s()
    if i == 'E':
        instance.roll_e()
    if i == 'W':
        instance.roll_w()
instance.print0()
