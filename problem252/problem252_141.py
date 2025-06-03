from itertools import accumulate

def bisect(ng, ok, judge, eps=1):
    while abs(ng-ok) > eps:
        m = (ng+ok)//2
        if judge(m):
            ok = m
        else:
            ng = m
    return ok

N,M = map(int,input().split())
A = sorted(map(int,input().split()))
acc = [0]+list(accumulate(A))

def judge(p):
    j = N
    cnt = 0
    for al in A:
        while j > 0 and al+A[j-1] >= p:
            j -= 1
        cnt += N-j
    return cnt <= M

p = bisect(0, A[-1]*2+1, judge)

j = N
cnt = 0
res = 0
nv = 0
max2 = lambda x,y: x if x > y else y
for al in A:
    while j > 0 and al+A[j-1] >= p:
        j -= 1
    cnt += N-j
    res += (N-j)*al + acc[-1]-acc[j]
    if j > 0:
        nv = max2(nv, al+A[j-1])

res += nv*(M-cnt)
print(res)