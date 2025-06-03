def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def l_b(x):
  ok = 0
  ng = 40
  while ng - ok > 1:
    mid = (ok+ng) // 2
    if n % (k ** mid) == 0:
      ok = mid
    else:
      ng = mid
  return x ** ok
n = int(input())
L = make_divisors(n)
ans = 0
for k in L:
  if k == 1:
    continue
  k_m = l_b(k)
  if (n // k_m) % k == 1:
    ans += 1
ans += len(make_divisors(n-1))
ans -= 1
print(ans)