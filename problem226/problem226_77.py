h, n = map(int, input().split())
a = list(map(int, input().split()))

a_sum = sum(a)

if h <= a_sum:
  print('Yes')
else:
  print('No')

