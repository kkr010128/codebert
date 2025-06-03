import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n = ni()
    a = nl()
    ok = -1
    ng = 10**18
    ans = -1
    while ng - ok > 1:
        v = mid = (ok + ng) // 2
        c = 0
        cnt = 0
        for x in a[:0:-1]:
            cnt += c + x
            c += x
            d = (c - 1) // 2 + 1
            if v > c - d:
                v -= c - d
                d = c
            elif v > 0:
                d += v
                v = 0
            c = d
        if a[0] + c > 1:
            ng = mid
        else:
            ok = mid
            ans = cnt + 1
    print(ans)
    return

solve()
