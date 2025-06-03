from collections import deque

n, m = map(int, input().split())
links = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

ans = [-1] * n
ans[0] = 0
q = deque([(0, 0)])
while q:
    room, prev = q.popleft()
    for next_ in links[room]:
        if ans[next_] < 0:
            ans[next_] = room
            q.append((next_, room))

print('Yes')
for i in range(1, n):
    print(ans[i] + 1)