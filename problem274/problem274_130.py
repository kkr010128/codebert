def f_sugoroku(INF=float('inf')):
    from collections import deque
    N, M = [int(i) for i in input().split()]
    S = input()

    dp = [INF] * (N + 1)  # [v]: 頂点 v からゴール到達までに最低何回かかるか
    dp[N] = 0

    q = deque([0])
    for i in range(N - 1, -1, -1):
        while True:
            if len(q) == 0:
                return '-1'

            if q[0] != INF and len(q) <= M:
                break
            q.popleft()

        if S[i] == '0':
            dp[i] = q[0] + 1
        q.append(dp[i])

    ans = []
    current = 0
    rest = dp[0]  # ゴールまであと何回ルーレットを回すか
    while current < N:
        # dp の値が rest から 1 減るまでインデックスを進める
        i = 1
        rest -= 1  # ルーレットを回した
        while dp[current + i] != rest:
            i += 1

        # ルーレットの出目を答えに追加し、現在位置を進める
        ans.append(i)
        current += i
    return ' '.join(map(str, ans))

print(f_sugoroku())