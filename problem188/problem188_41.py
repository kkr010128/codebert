from collections import deque
x,y,a,b,c=map(int,input().split())
p=sorted(list(map(int,input().split())),reverse=True)
q=sorted(list(map(int,input().split())),reverse=True)
r=deque(sorted(list(map(int,input().split())),reverse=True))
p=deque(p[:x])
q=deque(q[:y])
ans=sum(p)+sum(q)

while p[-1]<r[0] or q[-1]<r[0]:
  if p[-1]<q[-1]:
    ans+=r[0]-p[-1]
    r.popleft()
    p.pop()
  else:
    ans+=r[0]-q[-1]
    r.popleft()
    q.pop()
  if p==deque([]) or q==deque([]) or r==deque([]):
    break
if r==deque([]):
  pass
elif p==deque([]):
  while q[-1]<r[0]:
    ans+=r[0]-q[-1]
    r.popleft()
    q.pop()
    if q==deque([]) or r==deque([]):
      break
elif q==deque([]):
  while p[-1]<r[0]:
    ans+=r[0]-p[-1]
    r.popleft()
    p.pop()
    if p==deque([]) or r==deque([]):
      break
  
print(ans)