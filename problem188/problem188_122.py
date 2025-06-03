from heapq import heappop, heappush
X, Y, A, B, C = map(int, input().split())
h = []
for p in map(int, input().split()):
    heappush(h, (-p, 1))
for q in map(int, input().split()):
    heappush(h, (-q, 2))
for r in map(int, input().split()):
    heappush(h, (-r, 3))

ans = 0
cnt = 0
total = X + Y
while cnt < total:
    point, color = heappop(h)
    if color == 1:
        if X > 0:
            ans += -point
            X -= 1
            cnt += 1
    elif color == 2:
        if Y > 0:
            ans += -point
            Y -= 1
            cnt += 1
    elif color == 3:
        ans += -point
        cnt += 1
print(ans)
