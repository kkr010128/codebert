# Dice I

class Dice:
    def __init__(self, a1, a2, a3, a4, a5, a6):
        # サイコロを縦横にたどると書いてある数字(index1は真上、index3は真下の数字)
        self.v = [a5, a1, a2, a6] # 縦方向
        self.h = [a4, a1, a3, a6] # 横方向
        # print(self.v, self.h)

    # サイコロの上面の数字を表示
    def top(self):
        return self.v[1]

    # サイコロを北方向に倒す
    def north(self):
        newV = [self.v[1], self.v[2], self.v[3], self.v[0]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    # サイコロを南方向に倒す
    def south(self):
        newV = [self.v[3], self.v[0], self.v[1], self.v[2]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    # サイコロを東方向に倒す
    def east(self):
        newH = [self.h[3], self.h[0], self.h[1], self.h[2]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h

    # サイコロを西方向に倒す
    def west(self):
        newH = [self.h[1], self.h[2], self.h[3], self.h[0]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h


d = input().rstrip().split()
dice1 = Dice(d[0], d[1], d[2], d[3], d[4], d[5])

command = list(input().rstrip())
# print(command)

for i, a in enumerate(command):
    if a == 'N':
        dice1.north()
    elif a == 'S':
        dice1.south()
    elif a == 'E':
        dice1.east()
    elif a == 'W':
        dice1.west()
print(dice1.top())

