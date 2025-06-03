N, K = map(int, input().split())

L = [0] * K
R = [0] * K
for i in range(0, K):
    L[i], R[i] = map(int, input().split())

moves = [0] * N
moves[0] = 1

rui_wa = [0] * N
rui_wa[0] = 1

for i in range(1, N):
    for j in range(0, K):
        l = max(i - L[j], 0)
        r = max(i - R[j], 0)
        if i - L[j] < 0:
            continue

        moves[i] += (rui_wa[l] - rui_wa[r - 1]) % 998244353

    rui_wa[i] = (moves[i] + rui_wa[i - 1])  % 998244353



print(moves[N - 1] % 998244353)
