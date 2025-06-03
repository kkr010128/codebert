from sys import stdin
input = lambda : stdin.readline().strip()
ri = lambda : int(input())
ril = lambda : list(map(int, input().split()))

from collections import defaultdict

N = ri()
A = ril()
Q = ri()
s = sum(A)

d = defaultdict(int)
for a in A:
  d[a] += 1

ans = []
for i in range(Q):
  B, C = ril()
  s += (C - B) * d[B]
  d[C] += d[B]
  d[B] = 0
  ans.append(str(s))

print('\n'.join(ans))
