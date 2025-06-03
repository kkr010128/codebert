import numpy as np
import copy

d=int(input())
c=np.array(list(map(int,input().split())))
curc=copy.deepcopy(c)
s=[]
ans=[]
score=0
for i in range(d):
    s.append(list(map(int,input().split())))

for i in range(d):
    t=int(input())
    score+=s[i][t-1]
    curc[t-1]=0
    score-=sum(curc)
    curc+=c
    print(score)