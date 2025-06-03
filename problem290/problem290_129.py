def isok(arg):
    if arg < 0:
        return False
    count = 0
    for i in range(n):
        count += max(0,-(-(a[i]*f[i]-arg)//f[i]))
    if count <= k:
        return True
    else:
        return False

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isok(mid):
            ok = mid
        else:
            ng = mid
    return ok 

n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))
a.sort()
f.sort(reverse = True)
print(bisect(-1,10**12))
