a,b,c,k = map(int, input().split())

ans = 0

if k <= a:
  print(k)
  exit()

k -= a
ans += a

if k <= b:
  print(ans)
  exit()

k -= b
print(ans - k)