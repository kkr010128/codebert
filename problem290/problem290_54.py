import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = list(map(int,readline().split()))
F = list(map(int,readline().split()))
A.sort()
F.sort(reverse=True)

ng = -1
ok = 10**12+100
while ok - ng > 1:
    mid = (ok + ng) // 2
    if sum(max(0,a-mid//f) for a,f in zip(A,F)) <= K:
        ok = mid
    else:
        ng = mid
print(ok)
