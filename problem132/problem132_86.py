import sys
from itertools import accumulate

def solve(n,k,a):
    for _ in range(k):
        if a==[n]*n:    return a
        t = [0]*(n+1)
        for i,x in enumerate(a):
            t[max(0,i-x)] += 1
            t[min(n,i+x+1)] -=1
        a = list(accumulate(t))[:-1]
    return a

n,k = map(int,sys.stdin.readline().rstrip().split())
a = list(map(int,sys.stdin.readline().rstrip().split()))

print(*solve(n,k,a))