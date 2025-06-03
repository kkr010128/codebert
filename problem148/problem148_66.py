a, b, c, k = map(int,input().split())
ans = 0

if k - a > 0:
  ans = ans + a
  k = k - a               
  if k - b > 0:
    k = k -b
    ans = ans - k 
else:
  ans = ans + k
                 
print(ans)                 