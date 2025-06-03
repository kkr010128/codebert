N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
G = [-1 for i in range(N+1)]

for i, v in enumerate(P):
    G[i+1] = (v, C[v-1])

ans = -float("inf")

for i in range(1, N+1):
    loop = []
    S = i
    visited = [False for i in range(N+1)]
    while visited[S] == False:
        loop.append(G[S][-1])
        visited[S] = True
        S = G[S][0]

    circle_sum = sum(loop)
    this_case_ans = -float("inf")

    if circle_sum < 0:
        pass_sum = 0
        for i in range(len(loop)):
            pass_sum += loop[i]
            this_case_ans = max(this_case_ans, pass_sum)
        ans = max(ans, this_case_ans)
        continue

    else:
        L = len(loop)
        for i in range(1, L):
            loop[i] += loop[i-1]
        loop.insert(0, -float("inf"))
        for i in range(1, L+1):
            loop[i] = max(loop[i], loop[i-1])
        loop[0] = 0
        if K//L > 0:
            this_case_ans = max(K//L * circle_sum +
                                loop[K % L], (K//L-1)*circle_sum + loop[-1])
        else:
            for i in range(1, K+1):
                this_case_ans = max(this_case_ans, loop[i])
        ans = max(ans, this_case_ans)

print(ans)