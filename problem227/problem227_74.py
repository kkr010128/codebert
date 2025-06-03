def resolve():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    h = sorted(H)[::-1]
    ans = h[K:]
    print(sum(ans))
resolve()