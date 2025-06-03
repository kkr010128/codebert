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
        print(score)
    return score

def main():
    start=time()
    d,*s=map(int,open(0).read().split())
    s=int64(s)
    func(s,s[-d:]-1)
main()