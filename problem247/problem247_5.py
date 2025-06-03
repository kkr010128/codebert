import math
from functools import reduce
from copy import deepcopy
n,m = map(int,input().split())
A = list(map(int,input().split()))
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)
Acopy = deepcopy(A)
flag = -1
for i in range(n):
  cnt = 0
  while True:
    if Acopy[i] % 2 == 1:
      break
    else:
      Acopy[i] //= 2
      cnt += 1
  if i == 0:
    flag = cnt
  else:
    if flag != cnt:
      print(0)
      break
else:
  A = [a//2 for a in A]
  lcm = lcm_list(A)
  print((lcm+m)//2//lcm)
