def resolve():
    n, r = list(map(int, input().split()))

    if n > 10:
        ans = r
    else:
        ans = r + 100 * (10 - n)
    print(ans)
resolve()