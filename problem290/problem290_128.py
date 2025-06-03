def solve():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Fs = list(map(int, input().split()))

    As.sort()
    Fs.sort(reverse=True)

    def isOK(score):
        d = 0
        for A, F in zip(As, Fs):
            if A*F > score:
                d += -(-(A*F-score) // F)
        return d <= K

    ng, ok = -1, 10**12
    while abs(ok-ng) > 1:
        mid = (ng+ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


solve()
