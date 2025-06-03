from collections import deque
s = input()
q = int(input())
r = False
S = deque(s)
for _ in range(q):
  d = list(input().split())
  if len(d)==1:
    r = ~r
  else:
    if (d[1]=='1' and ~r) or (d[1]=='2' and r):
      S.appendleft(d[2])
    else:
      S.append(d[2])
s = ''.join(S)
if r:
  s = s[::-1]
print(s)