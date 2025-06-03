def MAIN():
    n = int(input())
    ans = [[i, 0, 0] for i in range((n + 1))]
    G = [[] for _ in range((n + 1))]
    for _ in range(n):
        u, k, *v = map(int, input().split())
        G[u] = v
    cnt = 1
    def dfs(u):
        nonlocal ans
        if ans[u][1] != 0:
            return
        nonlocal cnt
        ans[u][1] = cnt
        cnt += 1
        for v in G[u]:
            dfs(v)
        ans[u][2] = cnt
        cnt += 1
    for i in range(1, n + 1):
        if ans[i][1] == 0:
            dfs(i)
    for i in range(1, n + 1):
        print(" ".join(map(str, ans[i])))
MAIN()

