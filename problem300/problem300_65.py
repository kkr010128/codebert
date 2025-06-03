from fractions import gcd
A, B = map(int, input().split())
g = gcd(A, B)
ans = 1
n = 2
while g > 1:
  if n * n > g:
    ans += 1
    break
  if g % n == 0:
    ans += 1
  while g % n == 0:
    g //= n
  n += 1
print(ans)
