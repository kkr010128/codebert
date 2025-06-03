def resolve():
    N, D = map(int, input().split())

    cnt = 0
    for n in range(N):
        x, y = map(int, input().split())
        d = (x ** 2 + y ** 2) ** 0.5
        if d <= D:
            cnt += 1

    print(cnt)
resolve()