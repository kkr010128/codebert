H,N = map(int,input().split())
A = list(map(int,input().split()))
def battle(a,n):
  ans = 0
  for i in range(n):
    ans += a[i]
  return ans
    
if H <= battle(A,N):
  print("Yes")
else:
  print("No")