n = int(input())

ranges = []

for i in range(n):
    x, l = map(int, input().split())
    ranges.append([max(x-l, 0), x+l])

ranges.sort(key=lambda x: x[1])

start = 0
ans = 0
for range in ranges:
    if range[0] >= start:
        start = range[1]
        ans += 1

print(ans)