import collections 
h,w,k = [int(x) for x in input().split()]
s = [list(input()) for _ in range(h)]
a = [[0]*w for _ in range(h)]
cnt= 1
for i in range(h):
  for j in range(w):
    if s[i][j]=="#":
      a[i][j]=cnt
      cnt+=1
for i in range(h):
  for j in range(1,w):
    if a[i][j]==0:
      a[i][j]=a[i][j-1]
for i in range(h):
  for j in range(w-2,-1,-1):
    if a[i][j]==0:
      a[i][j]=a[i][j+1]
for j in range(w):
  for i in range(1,h):
    if a[i][j]==0:
      a[i][j]=a[i-1][j]
for j in range(w):
  for i in range(h-2,-1,-1):
    if a[i][j]==0:
      a[i][j]=a[i+1][j]
for i in a:
  print(*i)