n = int(input())
p = [220000] + list(map(int, input().split()))

cnt = 0
m = 220000
for i in range(1, n+1):
    now = p[i]
    m = min(m, now)
    if now == m:
        cnt += 1
print(cnt)