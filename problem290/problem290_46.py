N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
A.sort()
F.sort(reverse=True)
ng = -1
ok = 10**12+100
while ok - ng > 1:
    mid = (ok + ng) // 2
    c = 0
    for a,f in zip(A,F):
        c += max(0,a-mid//f)
    if c <= K:
        ok = mid
    else:
        ng = mid
print(ok)