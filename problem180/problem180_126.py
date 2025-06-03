n, k = map(int, input().split())

if n % k == 0:
  print(0)
else: 
  ans = n % k
  #print(ans)
  while ans > k//2:
    n = abs(ans - k)
    ans = min(n, ans)
  print(ans)