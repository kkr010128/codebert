N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print(0)
else:
    S, LUT, ans = [0], {0: 1}, 0
    for a in A:
        S.append(S[-1] + a)
    for i in range(1, N + 1):
        p = (S[i] - i) % K
        ans += LUT.get(p, 0)
        LUT[p] = LUT.get(p, 0) + 1
        if i - K + 1 >= 0:
            LUT[(S[i - K + 1] - i + K - 1) % K] -= 1
    print(ans)
