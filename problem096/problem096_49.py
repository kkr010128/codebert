def resolve():
    N, D = map(int, input().split())
    P = [list(map(int, input().split())) for x in range(N)]

    cnt = 0
    for p in P:
        d = (p[0] ** 2 + p[1] ** 2) ** 0.5
        if d <= D:
            cnt += 1

    print(cnt)
resolve()