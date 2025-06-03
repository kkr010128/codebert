import sys

N=int(input())
A = list(map(int,input().split()))
 
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

if gcd_list(A) > 1:
    print("not coprime")
    sys.exit()

D = [i for i in range(max(A)+1)] #iを割り切る最小の素数を格納
p = 2
 
while(p*p<=max(A)):
    if D[p]==p:
        for i in range(2*p,max(A)+1,p):
            if D[i]==i:
                D[i]=p
 
    p+=1
    
prime = set()
for a in A:
    tmp=D[a]
    L=set()
    while(a>1):
        a=a//tmp
        L.add(tmp)
        tmp=D[a]

    for l in L:
        if l in prime:
            print("setwise coprime")
            sys.exit()
        else:
            prime.add(l)

print("pairwise coprime")