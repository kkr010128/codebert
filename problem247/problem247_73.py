# ABC150D

import sys
input=sys.stdin.readline
from math import gcd,ceil

def main():
    N,M=map(int,input().split())
    A=list(map(lambda x: int(x)//2,input().split()))
    lcm=A[0]
    for i in range(1,N):
        lcm=lcm*A[i]//gcd(lcm,A[i])
    allo=1
    for i in range(N):
        allo&=(lcm//A[i])%2
    if allo:
        print(ceil(int(M//lcm)/2))
    else:
        print(0)
    
    
if __name__=="__main__":
    main()
