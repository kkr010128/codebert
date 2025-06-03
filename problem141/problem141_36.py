from sys import exit
from collections import deque
N = int(input())
D = deque(map(int, input().split()))
if N == 0:
  d = D.pop()
  if d == 1:
    print(1)
  else:
    print(-1)
  exit()
R = [[] for i in range(N + 1)]
leaf = D.pop()
R[-1].append(leaf)
R[-1].append(leaf)
for i in range(N - 1, -1, -1):
  leaf = D.pop()
  R[i].append(R[i + 1][0]//2 + R[i + 1][0] % 2 + leaf)
  R[i].append(R[i + 1][1] + leaf)
  R[i].append(leaf)
if not(R[0][0] <= 1 <= R[0][1]):
  print(-1)
  exit()
node = 1
ans = 1
for i in range(1, N + 1):
  node = min(R[i][1], 2 * (node - R[i-1][2]))
  ans += node
print(ans)