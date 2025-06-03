import sys
from collections import deque

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
A = LI()
q = I()
m = LI()
ans = 0
partial_sum = set()
for i in range(2 ** n):
    bit = [i>>j&1 for j in range(n)]
    partial_sum.add(sum(A[k]*bit[k] for k in range(n)))
for x in m:
    print('yes' if x in partial_sum else 'no')

