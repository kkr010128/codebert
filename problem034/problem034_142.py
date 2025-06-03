class Dice:
    def __init__(self):
        self.up = 1
        self.under = 6
        self.N = 5
        self.W = 4
        self.E = 3
        self.S = 2

    def roll(self, d):#d => direction
        if d == "N":
            tmp = self.up
            self.up = self.S
            self.S = self.under
            self.under = self.N
            self.N = tmp
        elif d == "W":
            tmp = self.up
            self.up = self.E
            self.E = self.under
            self.under = self.W
            self.W = tmp
        elif d == "E":
            tmp = self.up
            self.up = self.W
            self.W = self.under
            self.under = self.E
            self.E = tmp
        elif d == "S":
            tmp = self.up
            self.up = self.N
            self.N = self.under
            self.under = self.S
            self.S = tmp

    def getUpward(self):
        return self.up

    def setRoll(self,up,under,N,W,E,S):
        self.up = up
        self.under = under
        self.N = N
        self.W = W
        self.E = E
        self.S = S

    def rotate(self):#crockwise
        tmp = self.S
        self.S = self.E
        self.E = self.N
        self.N = self.W
        self.W = tmp

    def getE(self, up, S):
        '''
        
        :param up:num 
        :param S: num
        :return: num
        '''
        count = 0
        while True:
            if self.up == up:
                break
            if count != 3:
                self.roll("N")
                count += 1
            else:
                self.roll("E")
        while True:
            if self.S == S:
                break
            self.rotate()
        return self.E



myd = Dice()
myd.up, myd.S, myd.E, myd.W, myd.N, myd.under = map(int,input().split())
n = int(input())
for i in range(n):
    up, S = map(int,input().split())
    print(myd.getE(up,S))