import bisect


def abc170c_forbidden_list():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(100):
        idx = bisect.bisect_left(p, x - i)
        if idx >= n or p[idx] != x - i:
            print(x - i)
            return
        idx = bisect.bisect_left(p, x + i)
        if idx >= n or p[idx] != x + i:
            print(x + i)
            return


abc170c_forbidden_list()