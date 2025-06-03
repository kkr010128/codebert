from collections import deque
N, M = map(int, input().split())
Mlist = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    Mlist[a].append(b)
    Mlist[b].append(a)

ans = [0] * (N+1)

d = deque()
d.append(1)
count = 0
while count != N:
    Q = d.popleft()
    for i in Mlist[Q]:
        if ans[i] == 0:
            ans[i] = Q
            d.append(i)
            count = count+1
print('Yes')
for i in range(N-1):
    print(ans[i+2])
