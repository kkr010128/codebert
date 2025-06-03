from time import time
from random import randint

from numba import njit
from numpy import int64

@njit('i8(i8[:],i8[:])')
def func(s,x):
    last=[0]*26
    score=0
    for i,v in enumerate(x,1):
        last[v]=i
        c=0
        for j in range(26):
            c+=s[j]*(i-last[j])
        score=score+s[i*26+v]-c
    return score

def main():
    start=time()
    d,*s=map(int,open(0).read().split())
    s=int64(s)
    x=int64(([*range(26)]*15)[:d])
    M=func(s,x)
    while time()-start<1.3:
        y=x.copy()
        y[randint(0,d-1)]=randint(0,25)
        t=func(s,y)
        if t>M:
            M=t
            x=y
    print(*x+1,sep='\n')

main()