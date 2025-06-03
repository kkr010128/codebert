def keyence20_c():
    N, K, S = map(int, input().split())
    if S < 10**9:
        arr = [S] * K + [S+1] * (N-K)
    else:
        arr = [S] * K + [1] * (N-K)
    ans = ' '.join(map(str, arr))
    print(ans)

keyence20_c()