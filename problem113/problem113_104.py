import random
import numpy as np


D=int(input())
C=np.array(list(map(int,input().split())))
S=[]
for _ in range(D):
    S.append(list(map(int,input().split())))




l=np.zeros(26,int)

def decrease(d):
    return np.dot(C,(d-l))

def pick(i,l):
    diff=[]
    ll=l.copy()
    for j in range(26):
        ll[j]=i
        diff.append(S[i][j]-decrease(i))
    return np.argmax(diff)+1


for i in range(D):
    p=pick(i,l)
    print(p)
    l[p-1]=i+1