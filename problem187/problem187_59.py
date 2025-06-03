n, x, y = map(int, input().split())
x -= 1
y -= 1
dist = [0]*(n-1)
for start in range(n):
    for end in range(start+1, n):
        dst = min(end-start, abs(x-start) + abs(end-y) + 1)
        dist[dst-1] += 1

for d in dist:
    print(d)