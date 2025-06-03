N, M = map(int, input().split())

ans = []
n = M // 2
m = 2 * n + 1
l = 2 * M + 1
for i in range(n):
    ans.append([i + 1, m - i])

for i in range(M - n):
    ans.append([m + i + 1, l - i])

for v in ans:
    print(*v)
