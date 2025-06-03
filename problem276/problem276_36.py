import itertools
n = int(input())
a = list(itertools.accumulate(list(map(int, input().split()))))
sum_a = a[-1]
res = 2020202020
for i in range(n):
  res = min(res, abs(sum_a - a[i]*2))
print(res)
