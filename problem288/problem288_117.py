import math
N = int(input())
n_max = int(math.sqrt(N))
a = []
for i in range(1,n_max + 1):
  if N % i == 0:
    a.append(i)
ans = 2 * N
for i in a:
  if (i + (N // i) - 2) < ans:
    ans = i + (N // i) - 2
print(ans)
