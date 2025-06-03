a, b = list(map(int, input().split(' ')))
def gcd(l, s):
  return l if s == 0 else gcd(s, l % s)

temp = gcd(a, b)

ans = 0
for i in range(2,1000000):
  if temp % i == 0:
    ans += 1
    while temp % i == 0:
      temp = temp // i
  if temp == 1:
    break
if temp != 1:
  ans += 1

print(ans+1)