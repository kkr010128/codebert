from collections import deque

n, m = map(int, input().split())
room = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    room[a-1].append(b)
    room[b-1].append(a)

point = [0 for i in range(n)]
d = deque([0])

while len(d) > 0:
    p = d.popleft()
    for v in room[p]:
        if point[v-1] == 0:
            d.append(v-1)
            point[v-1] = p+1

print('Yes')
for i in range(1, n):
    print(point[i])
