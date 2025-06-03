from collections import deque
n,m=map(int,input().split())
s=deque(input())
a=0
for i in range(n+1):
  if s[i]=="1":
    a=a+1
    if a==m:
      print(-1)
      break
  else:
    a=0
if a==0:
  b=deque([])
  d=n
  while d>0:
    if d<=m:
      b.appendleft(d)
      d=0
    else:
      i=m
      while i>0:
        if s[d-i]=="1":
          i=i-1
        else:
          b.appendleft(i)
          d=d-i
          for j in range(i):
            s.pop()
          break
  for i in range(len(b)):
    print(b[i],end=" ")