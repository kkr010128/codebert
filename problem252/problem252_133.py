from sys import stdout
import bisect
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def f(x):
    sm = 0
    for i in range(n-1,-1,-1):
        j = bisect.bisect_left(a,x-a[i])
        sm += n-j
        if sm>=m:
            return True
    return False

n,m = inm()
a = inl()
a.sort()
acc = [0]*(n+1)
for i in range(n-1,-1,-1):
    acc[i] = acc[i+1]+a[i]
mn = 2*min(a)
mx = 2*max(a)+1
while mx-mn>=2:
    mid = (mx+mn)//2
    if f(mid):
        mn = mid
    else:
        mx = mid
# mn is the m-th
# sum and cnt upto mn+1
sm = cnt = 0
for i in range(n):
    j = bisect.bisect_left(a,mx-a[i])
    sm += acc[j]+(n-j)*a[i]
    cnt += n-j
print(sm+mn*(m-cnt))
