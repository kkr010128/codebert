def isok(t):
    cnt = 0
    for i in range(n):
        cnt += max(a[i] - t // f[i], 0)
        if cnt > k:
            return False
    return True 

n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))
a.sort(reverse = 1)
f.sort()
ok = a[0] * f[-1]
ng = -1
bool = True
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
    #print(ng,mid,ok)
print(ok)
