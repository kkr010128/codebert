H=int(input())

Q=[]
import math
for i in range(10000):
    if H>1:
        H=H//2
        Q.append(H)
    elif H==1:
        break
Q.sort()
S=0
a=1
for i in range(len(Q)):
    a=2*a+1
print(a)