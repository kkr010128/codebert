def check(m):
    global n, k, w, presum
    s = 0
    for j in range(k):
        ok = s
        ng = n + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if presum[mid] - presum[s] <= m:
                ok = mid
            else:
                ng = mid
        s = ok
    if s == n:
        return True
    else:
        return False


def resolve():
    global n, k, w, presum
    n, k = [int(i) for i in input().split()]
    w = [int(input()) for _ in range(n)]
    presum = [0 for _ in range(n + 1)]
    for i in range(n):
        presum[i + 1] = presum[i] + w[i]
    if n <= k:
        print(max(w))
        return
    ok = 100000 * 10000
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


resolve()

