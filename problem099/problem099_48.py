N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(mid):
    s = 0
    for j in range(N):
        if mid < A[j]:
            s += A[j] // mid
    return s <= K

max_A = 10**9 + 1
ng = 0
ok = max_A

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
        
print(ok)