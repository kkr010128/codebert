import math

N, K = map(int, input().split())
A = list(map(float, input().split()))


min_A = 0
max_A = 10**10

while( max_A - min_A > 1):
  now = (min_A + max_A) // 2
  temp = 0
  for i in A:
    if i > now:
      temp += (i // now)
  if temp > K:
    min_A = now
  else:
    max_A = now

print(int(min_A) + 1)