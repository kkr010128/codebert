from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = li()
N = []
N.append(n[0])

for i in range(1,3,1):
    if n[i] in N: continue
    N.append(n[i])

if len(N) == 2:
    print('Yes')
else:
    print('No')