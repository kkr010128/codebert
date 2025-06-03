import sys
input = sys.stdin.readline
n,d,a = map(int,input().split())
attack = [0 for _ in range(n)]
event = []
for i in range(n):
  x,h = map(int,input().split())
  h = (h-1)//a+1
  event.append([x-d,0,h,i])
  event.append([x+d,1,h,i])
event.sort()
#print(event)
ans = 0
now = 0
for j in range(2*n):
  x,m,h,i = event[j]
  if m == 0:
    if h > now:
      attack[i] += h-now
      ans += h-now
      now = h
  else:
    now -= attack[i]
print(ans)