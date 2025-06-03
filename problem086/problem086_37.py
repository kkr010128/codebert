n, x, t = list(map(int, input().split()))
tmp = int(n / x)
tmp2 = n % x
if tmp2 > 0:
  tmp += 1
print(tmp * t)