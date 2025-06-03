import collections
import math

def c2(x):
  c = math.factorial(x) // (math.factorial(x-2)*2)
  return c

n = int(input())

a = list(map(int, input().split()))

adic = collections.Counter(a)

cnt = 0

for i in adic:
  num = adic[i]
  if num > 1:
    cnt += c2(num)

for i in a:
  num = adic[i]
  if num == 1:
    print(cnt)
  else:
    print(cnt - (num-1))