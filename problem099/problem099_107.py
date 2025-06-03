N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(n):
    cnt = 0
    for a in A:
        if n >= a:
            continue
        cnt += a // n
    return cnt <= K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0, 10**9+1))
