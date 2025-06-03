import random

class Dice():
    def __init__(self):
        self.face = [i for i in range(6)]
        self.memo = [i for i in range(6)]

    def setface(self,initface):
        for i in range(6):
            self.face[i] = initface[i]

    def roll(self,direction):
        for i in range(6):
            self.memo[i] = self.face[i]
        index = {'E':(3,1,0,5,4,2),'N':(1,5,2,3,0,4),'S':(4,0,2,3,5,1),'W':(2,1,5,0,4,3)}
        for i in range(6):
            self.face[i] = self.memo[index[direction][i]]

    def top(self):
        return self.face[0]

dice = Dice()
initface = list(map(int,input().split()))
dice.setface(initface)
q = int(input())
for _ in range(q):
    u,f = map(int,input().split())
    while True:
        dice.roll(['E','N','S','W'][random.randint(0,3)])
        if dice.face[0]==u and dice.face[1]==f:
            print(dice.face[2])
            break
