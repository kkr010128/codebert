import statistics
import math

N = int(input())
listA = [0] * N
listB = [0] * N
idx = 0
for i in range(N):
  listA[idx],listB[idx] = map(int, input().split())
  idx += 1

medianA = 0
medianB = 0
ans = 0
if N%2 == 0:
  medianA = statistics.median(listA)
  medianB = statistics.median(listB)
  ans = (medianB - medianA) * 2 + 1
else:
  medianA = statistics.median(listA)
  medianB = statistics.median(listB)
  ans = medianB - medianA + 1

print(int(ans))