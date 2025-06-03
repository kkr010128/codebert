N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
    cnt = 0
    for a in A:
        cnt += a // x
        if a % x == 0:
            cnt -= 1
    return cnt <= K

ng = 0
ok = 10**9
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)