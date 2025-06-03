import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

x,y = map(int,input().split())
for turu in range(x+1):
  kame = x-turu
  if kame * 4 + turu * 2 == y:
    print("Yes")
    exit()
print("No")