class Dice:
    def __init__(self,u,s,e,w,n,d):
        self.u = u
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.d = d
    def rot(self,way):
        if way == 0:
            c = self.u
            self.u = self.n
            self.n = self.d
            self.d = self.s
            self.s = c
        if way == 1:
            c = self.e
            self.e = self.n
            self.n = self.w
            self.w = self.s
            self.s = c
        if way == 2:
            c = self.w
            self.w = self.d
            self.d = self.e
            self.e = self.u
            self.u = c
u,s,e,w,n,d = map(int,input().split())
dice = Dice(u,s,e,w,n,d)
questions = int(input())
for q in range(questions):
    top, south = map(int,input().split())
    flag = 0
    count = 0
    while True:
        for v in range(5):
            if dice.u == top and dice.s == south:
                print(dice.e)
                flag = 1
                break
            else:
                dice.rot(0)
        if flag:
            break
        elif count == 5:
            dice.rot(2)
            count = 0
        else:
            dice.rot(1)
            count += 1
    
    
    
