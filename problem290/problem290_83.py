n, k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))
a.sort()
f.sort(reverse = True)
af = [a[i]*f[i] for i in range(n)]

def check(x):
  r = 0
  for i in range(n):
    r += (max(0,(af[i]-x))+f[i]-1)//f[i]
  #print(r, x)
  if r<=k:
    return True
  else:
    return False
ok = 10**12+1
ng = -1
while ok-ng>1:
  mid = (ok + ng)//2
  if check(mid):
    ok = mid
  else:
    ng = mid
print(ok)