def resolve():
    A, B, M = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x, y, c = [], [], []
    dis = []
    for i in range(M):
        xt, yt, ct = list(map(int, input().split()))
        dis.append(a[xt-1] + b[yt-1] - ct)
        x.append(xt)
        y.append(yt)
        c.append(ct)

    a.sort()
    b.sort()
    dis.sort()
    ans = min(a[0] + b[0], dis[0])
    print(ans)

    return


resolve()