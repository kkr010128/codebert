# D - String Formation
from collections import deque
S = input()
Q = int(input())
now = 1
tmp = [deque([]),deque([])]
for _ in range(Q):
    t = list(input().split())
    if t[0]=='1':
        now = 1+(now==1)
    else:
        if int(t[1])==now:
            tmp[0].append(t[2])
        else:
            tmp[1].append(t[2])
ans = ''
if now==1:
    i,j = 0,1
else:
    i,j = 1,0
while len(tmp[i])>0:
    ans += tmp[i].pop()
if now==2:
    S = S[::-1]
ans += S
while len(tmp[j])>0:
    ans += tmp[j].popleft()
print(ans)