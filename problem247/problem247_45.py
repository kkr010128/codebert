from fractions import gcd
n, m = map(int, input().split())
lst = list(map(int, input().split()))

norm = 0
tmp = lst[0]
while tmp%2 == 0:
  tmp = tmp//2
  norm += 1

for i in range(n):
  count = 0
  tmp = lst[i]
  while tmp%2 == 0:
    tmp = tmp//2
    count += 1
  if norm != count:
    print(0)
    exit()
  lst[i] = lst[i]//2
    
lst = sorted(list(set(lst)))

def lcm(a, b): # a, b の最大公約数を求める
  return(a*b//gcd(a, b))

def lcms(List): # list[a[0], a[1], ... , a[n]]の最小公倍数を求める
  if len(List) == 1:
    return List[0]
  ans = lcm(List[0], List[1])
  for i in range(2, len(List)):
    ans = lcm(ans, List[i])
  return ans
    
lcm = lcms(lst)
ans = m//lcm
if ans%2 == 0:
  ans = ans//2
else:
  ans = ans//2 + 1
print(ans)