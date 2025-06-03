def solve():
    N, K = map(int, input().split())
    *P, = map(int, input().split())
    *C, = map(int, input().split())
    ans = -float("inf")

    for pos in range(N):
        used = [-1] * N
        cost = [0] * (N+1)

        for k in range(N+1):
            if k:
                cost[k] = cost[k-1] + C[pos]
            if used[pos] >= 0:
                loop_size = k-used[pos]
                break
            used[pos] = k
            pos = P[pos] - 1
        if cost[loop_size] <= 0:
            ans = max(ans, max(cost[1:K+1]))
        else:
            a, b = divmod(K, loop_size)
            v1 = cost[loop_size] * (a-1) + max(cost[:K+1])
            v2 = cost[loop_size] * a + max(cost[:b+1])
            ans = max(ans, max(v1, v2) if a else v2)

    print(ans)

solve()
