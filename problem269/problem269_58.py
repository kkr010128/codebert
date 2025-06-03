T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

from math import *

x = A1*T1 + A2*T2 - (B1*T1 + B2*T2)
y = A1*T1 - B1*T1
if(x ==0 or y==0):
    print('infinity')
elif(y * x > 0):
    print(0)
else:
    z = floor(abs(y) / abs(x))
    if abs(y) == z * abs(x):
        print(floor(abs(y)/abs(x))*2)
    else:
        print(floor(abs(y)/abs(x))*2+1)

