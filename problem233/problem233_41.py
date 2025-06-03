n = int(input())
p = list(map(int, input().split()))

lower = p[0]
cnt = 1
for i in range(1, n):
    if lower > p[i]:
        cnt += 1
        lower = min(lower, p[i])

print(cnt)

