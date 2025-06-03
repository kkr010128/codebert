from math import *
from copy import deepcopy
A,B = map(int,input().split())
C = gcd(A,B)
E = deepcopy(C)
D = set()
for i in range(2,floor(sqrt(E))+1):
    while True:
        if C/i != (C/i)//1:
            break
        D.add(i)
        C /= i
if C != 1:
    D.add(int(C))
print(len(D)+1)