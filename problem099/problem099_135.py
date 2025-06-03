n, k = map(int, input().split())
a = list(map(int, input().split()))


def is_ok(l):
    cnt = 0
    for L in a:
        cnt += L // l - 1
        if L % l != 0:
            cnt += 1
    return cnt <= k


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, max(a)))