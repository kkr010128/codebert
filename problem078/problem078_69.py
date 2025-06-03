n = int(input())

if n<2:
  ans = 0
else:
  ans =(10**n-(9**n)*2+8**n)%(10**9+7)

print(ans)