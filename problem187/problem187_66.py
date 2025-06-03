import sys
sys.setrecursionlimit(10000000)

n,x,y=map(int,input().split())
x-=1
y-=1
res=[0]*n
for i in range(n):
  for j in range(i+1,n):
    m = min(j-i, abs(i-x)+abs(j-y)+1, abs(i-y)+abs(j-x)+1)
    res[m]+=1
for i in range(1,n):
  print(res[i])