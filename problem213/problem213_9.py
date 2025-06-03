import math
N = int(input())
X = list(map(int, input().split()))

def average(a):
  return sum(a) / len(a)

avg = average(X)

res = 0
if avg - int(avg) >= 0.5:
  for i in X:
    res += (i - math.ceil(avg)) **2
else:
  for i in X:
    res += (i - math.floor(avg)) ** 2
print(res)