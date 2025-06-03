from math import *
n=int(input())
f=0
for i in range(n,100009):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
        if(c>=3):
            break
    if(c==2):
        print(i)
        f=1
        exit()
