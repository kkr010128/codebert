import sys
import bisect
input = sys.stdin.readline

class Bisect(object):
    def bisect_max(self, reva, func,M):
        ok = 0 # exist
        ng = 2*(10**5)+1 # not exist
        while abs(ok-ng) > 1:
            cnt = (ok + ng) // 2
            if func(cnt,reva,M):
                ok = cnt
            else:
                ng = cnt
        return ok

def solve1(tgt,reva,M):
    res=0
    n = len(reva)
    if (n - bisect.bisect_left(reva,tgt-reva[n-1]))*n < M:
        return False
    for i in range(n):
        res += n - bisect.bisect_left(reva,tgt-reva[n-i-1])
        if M <= res:
            return True
    return False

N,M = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
reva = a[::-1]
bs = Bisect()
Kmax = (bs.bisect_max(reva,solve1,M))

r=[0]
for i in range(N):
    r.append(r[i]+a[i])

res = 0
cnt = 0
t = 0
for i in range(N):
    tmp = bisect.bisect_left(reva,Kmax-reva[N-i-1])
    tmp2 = bisect.bisect_right(reva,Kmax-reva[N-i-1])
    if tmp!=tmp2:
        t = 1
    tmp = N - tmp
    cnt += tmp
    res += tmp*a[i]+r[tmp]
if t==1:
    res -= (cnt-M)*Kmax
print(res)
