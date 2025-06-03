# coding: utf-8
# Your code here!

class Dice:
    def __init__(self,lst):
        self.face=lst
        self.order="NNNNWNNNWNNNENNNENNNWNNN"
    
    def roll(self,x):
        tmp=self.face
        if x=="E":
            self.face=[tmp[3],tmp[1],tmp[0],tmp[5],tmp[4],tmp[2]]
        if x=="W":
            self.face=[tmp[2],tmp[1],tmp[5],tmp[0],tmp[4],tmp[3]]
        if x=="N":
            self.face=[tmp[1],tmp[5],tmp[2],tmp[3],tmp[0],tmp[4]]
        if x=="S":
            self.face=[tmp[4],tmp[0],tmp[2],tmp[3],tmp[5],tmp[1]]
    
    def showDown(self):
        return self.face[0]
    
    def query(self,lst):
        tmp=self.face
        ans=-1
        for i in self.order:
            self.roll(i)
            if self.face[0]==lst[0] and self.face[1]==lst[1]:
                ans=self.face[2]
                break
        self.face=tmp
        return ans
    
dice=Dice(list(map(int,input().split(" "))))
num=int(input())
q=[list(map(int,input().split())) for i in range(num)]
for i in q:
    print(dice.query(i))
