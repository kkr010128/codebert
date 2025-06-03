from math import *
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
def is_ok(arg):
    tmp=0
    for i in a:
        tmp+=ceil(i/arg)-1
    return tmp<=k


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(0, max(a)))