from collections import deque
N = int(input())
c = [chr(ord("a") + i) for i in range(26)]
q = deque("a")
ans = []
while q:
    s = q.pop()
    if len(s) == N:
        ans.append(s)
        continue
    for x in c[:c.index(max(s)) + 2]:
        q.append(s + x)
[print(a) for a in sorted(ans)]