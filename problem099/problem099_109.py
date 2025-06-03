N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(L):
    count = 0
    for a in A:
        count += a // L
        if a % L == 0:
            count -= 1
    return count <= K

ng = 0
ok = max(A)
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
