n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
if sum(a) >n:
  ans = -1
else:
  ans = n-sum(a)
print(ans)