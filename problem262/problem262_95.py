from itertools import *
N = int(input())
H = []
A = []

for i in range(N):
  for j in range(int(input())):
    x,y = map(int, input().split())
    H+=[[i,x-1,y]]

for P in product([0,1],repeat=N):
  for h in H:
    if P[h[0]]==1 and P[h[1]]!=h[2]:
      break
  else:
    A+=[sum(P)]

print(max(A))