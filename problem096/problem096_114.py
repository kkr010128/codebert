a, b = map(int, input().split())
import numpy
count = 0
for i in range(a):
  c, d = map(int, input().split())
  e = c ** 2 + d ** 2
  if numpy.sqrt(e) <= b:
    count += 1
print(count)