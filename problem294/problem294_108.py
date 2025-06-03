n = int(input())
ls = list(map(int,input().split()))
ls.sort()
p = 0
def is_ok(arg,l):
    return ls[arg] < l
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        l = ls[i] + ls[j]
        if is_ok(mid,l):
            ok = mid
        else:
            ng = mid
    return ok
for i in range(n-2):
    for j in range(i+1,n-1):
        ng = n
        ok = j
        m = meguru_bisect(ng, ok)
        p += m-j 
print(p)
