n, x, y = map(int, input().split())
x -= 1
y -= 1
cnt = [0] * n
for i in range(n-1):
    for j in range(i+1, n):
        direct = j - i
        detour = abs(x-i) + abs(y-j) + 1
        d = min(direct, detour)
        cnt[d] += 1
for k in range(1, n):
    print(cnt[k])