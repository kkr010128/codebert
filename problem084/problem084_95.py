import sys
import resource

def root(x):
  if par[x] == x:
    return x
  par[x] = root(par[x])
  return par[x]

def union(x, y):
  rx = root(x)
  ry = root(y)
  if rx != ry:
    par[rx] = ry
  return 0

sys.setrecursionlimit(10 ** 6)
n, m=map(int, input().split(" "))
par = list(range(n + 1))
for i in range(m):
  a, b = map(int, input().split(" "))
  union(a, b)
#print(par)
maxi = 0
count = 1
#print(par)
countpar = [0 for i in range(n + 1)]
#print(len(countpar), len(par))
for i in range(1, n + 1):
  countpar[root(par[i])] += 1
print(max(countpar))
#print(countpar, par)
