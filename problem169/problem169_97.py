import collections
n = int(input())
x = list(map(int, input().split()))

y = collections.Counter(x)

for i in range(1, len(x)+2):
  print(y[i], end = "\n")