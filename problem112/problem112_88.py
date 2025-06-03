def solve():
    MOD = 10**9 + 7
    INF = 10**10

    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    if K == N:
        ans = 1
        for A in As:
            ans *= A
            ans %= MOD
        print(ans)
        return

    As.sort(key=lambda x: abs(x))

    if max(As) < 0 and K%2 != 0:
        ans = 1
        for A in As[:K]:
            ans *= A
            ans %= MOD
        print(ans)
        return

    As.reverse()

    ans = 1
    sgn = 1
    for A in As[:K]:
        ans *= A
        ans %= MOD
        if A < 0:
            sgn *= -1
        elif A == 0:
            sgn = 0

    if sgn >= 0:
        print(ans)
        return

    maxNeg, maxNotNeg = -INF, -INF
    minNeg, minPos = INF, INF
    for A in As[:K]:
        if A < 0:
            maxNeg = max(maxNeg, A)
        if A > 0:
            minPos = min(minPos, A)
    for A in As[K:]:
        if A < 0:
            minNeg = min(minNeg, A)
        if A >= 0:
            maxNotNeg = max(maxNotNeg, A)

    if maxNeg == -INF or maxNotNeg == -INF:
        ans *= pow(minPos, MOD-2, MOD) * minNeg
        ans %= MOD
    elif minNeg == INF or minPos == INF:
        ans *= pow(maxNeg, MOD-2, MOD) * maxNotNeg
        ans %= MOD
    else:
        if abs(maxNeg)*abs(minNeg) >= abs(minPos)*abs(maxNotNeg):
            ans *= pow(minPos, MOD-2, MOD) * minNeg
            ans %= MOD
        else:
            ans *= pow(maxNeg, MOD-2, MOD) * maxNotNeg
            ans %= MOD

    print(ans)


solve()
