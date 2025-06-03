class Dice:
    def __init__(self):
        self.dice=[1,2,3,4,5,6] # up,front,right,left,back,front
    def set(self,l):
        self.dice=l
    def roll(self, s):
        import copy
        mat=((1,4,3,2),(5,0,1,1),(2,2,0,5),(3,3,5,0),(0,5,4,4),(4,1,2,3))
        l=copy.deepcopy(self.dice)
        if s == 'N': c = 0
        if s == 'S': c = 1
        if s == 'E': c = 2
        if s == 'W': c = 3
        for i in range(6):
            self.dice[i]=l[mat[i][c]]
    def get(self):
        return self.dice

import random
d=Dice()
d.set(list(map(int,input().split())))
for i in range(int(input())):
    u,f=map(int,input().split())
    while True:
        d.roll('NSEW'[random.randrange(4)])
        if d.get()[0]==u and d.get()[1]==f:
            print(d.get()[2])
            break