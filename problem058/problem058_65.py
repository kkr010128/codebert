def dfs(i, j, s):
    if j > 3:
        return
    if j == 3 and s == x:
        ans.append(1)

    for k in range(1, i):
        if s + k > x:
            break
        dfs(k, j + 1, s + k)

while True:
    ans = []
    n, x = map(int, input().split())
    if n == x == 0:
        break

    for i in range(3, n + 1):
        dfs(i, 1, i)

    print(sum(ans))
