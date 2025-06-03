def solve():
    MOD = 10**9 + 7

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

    pos0As, negAs = [], []
    for A in As:
        if A >= 0:
            pos0As.append(A)
        elif A < 0:
            negAs.append(A)
    pos0As.sort()
    negAs.sort(reverse=True)

    ans = 1
    rest = K
    while rest > 0:
        if rest == 1:
            ans *= pos0As.pop()
            rest -= 1
        else:
            if len(pos0As) < 2:
                ans *= negAs.pop()
                ans *= negAs.pop()
                rest -= 2
            elif len(negAs) < 2:
                ans *= pos0As.pop()
                rest -= 1
            else:
                pPos0 = pos0As[-1] * pos0As[-2]
                pNeg = negAs[-1] * negAs[-2]
                if pPos0 >= pNeg:
                    ans *= pos0As.pop()
                    rest -= 1
                else:
                    ans *= negAs.pop()
                    ans *= negAs.pop()
                    rest -= 2
        ans %= MOD

    print(ans)


solve()
