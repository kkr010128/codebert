import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

js = [None for _ in range(n)] # 周期とスコア増分

for s in range(n):
    if js[s]:
        continue
    m = s
    tmp = 0
    memo = [[] for _ in range(n)]
    i = 0
    while True:
        m = p[m] - 1
        tmp += c[m]
        memo[m].append((i, tmp))
        if len(memo[m]) > 1:
            js[m] = (memo[m][1][0] - memo[m][0][0], memo[m][1][1] - memo[m][0][1])
        if len(memo[m]) > 2:
            break
        i += 1

ans = -100000000000
for s in range(n):
    m = s
    tmp = 0
    visited = [0] * n
    for i in range(k):
        m = p[m] - 1
        if visited[m]:
            break
        visited[m] = 1
        tmp += c[m]
        if js[m] and js[m][1] > 0:
            ans = max(ans, tmp + js[m][1] * ((k - i - 1) // js[m][0]))
        else:
            ans = max(ans, tmp)
print(ans)
