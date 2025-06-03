import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
  

N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
  A[i] = A[i] // 2
  
p = 0
de_2 = 0
x = A[0]
while (p == 0):
  if x % 2 == 0:
    x = x // 2
    de_2 += 1
  else:
    p = 1
    
de = 2 ** de_2
for i in range(1, N):
  if A[i] % de == 0:
    if A[i] % (de * 2) != 0:
      continue
    else:
      print("0")
      quit()
  else:
    print("0")
    quit()
  
lcm = lcm_list(A)
p = M // lcm
if p % 2 == 0:
  ans = p // 2
else:
  ans = (p + 1) // 2
  
print(ans)


