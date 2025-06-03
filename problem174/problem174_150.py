K = int(input())
total = 0

def gcd2(a,b): #互除法
  while True:
    mod = a % b
    if mod == 0:
      return b
    a = b
    b = mod

memo = {}
def gcd(a,b,c):
  return gcd2(gcd2(a,b),c)
#  a,b,c = sorted([a,b,c])
#  if (a,b,c) not in memo:
#    val = gcd2(gcd2(a,b), c)
#    memo[(a,b,c)] = val
#    return val
#  return memo[(a,b,c)]

for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      g = gcd(a, b, c)
#      print(a,b,c, g)
      total += g

print(total)