x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

from collections import deque

p = sorted(p)[a-x:]
q = sorted(q)[b-y:]
t = deque(sorted(p+q))
r = deque(reversed(sorted(r)))
# print(t,r)

while r:
    if t[0] < r[0]:
        t.popleft()
        w = r.popleft()
        t.append(w)
    else:
        break

ans = sum(t)
print(ans)