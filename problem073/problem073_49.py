n = int(input())
ans = 0

for i in range(1, n):
  x = n//i
  y = x-1 if n==x*i else x
  ans += y
  
print(ans)