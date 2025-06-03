from collections import deque
def solve(n,t):
  q=deque([])
  for i in range(n):
    l=list(input().split())
    q.append(l)
  time=0
  while not len(q)==0:
    x=q.popleft()
    if int(x[1])-t>0:
      x[1]=str(int(x[1])-t)
      time+=t
      q.append(x)
    else:
      print(x[0]+" "+str(time+int(x[1])))
      time+=int(x[1])
n,t=map(int,input().split())
solve(n,t)
