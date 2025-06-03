import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,d = map(int,input().split())
for i in range(n):
  x,y = map(int,input().split())
  if x**2 + y ** 2 <= d**2:
    count += 1
print(count)