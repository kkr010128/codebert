import numpy

N = int(input())
A = list(map(int, input().split()))
res = numpy.cumsum(A)

if res[-1] % 2 == 0:
  L = res[-1]//2
  ans = [abs(r - L) for r in res]
  print(2*min(ans))
else:
  L1 = res[-1]//2
  L2 = L1 + 1
  ans = [min(abs(r - L1),abs(r-L2)) for r in res]
  print(2*min(ans)+1)