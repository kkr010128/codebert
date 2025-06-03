import math as m


EPS = 0.0000000001


def f(a, b, theta):
    if theta > m.pi/2 - EPS:
        return 0
    if a * m.tan(theta) <= b:
        ret = a * a * b - a * a * a * m.tan(theta) / 2
    else:
        ret = b * b / m.tan(theta) * a / 2
    return ret


def solve():
    a, b, x = map(int, input().split())
    ok = m.pi / 2
    ng = 0
    
    for _ in range(100):
        mid = (ok + ng) / 2
        if f(a, b, mid) < x:
            ok = mid
        else:
            ng = mid
    print(ok * 180 / m.pi)


if __name__ == "__main__":
    solve()