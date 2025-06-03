k = int(input())
from collections import deque

d = deque()
c = 0
for i in range(1, 10):
  d.append(i)

while True:
  tmp = d.popleft()
  c += 1
  if c == k:
    ans = tmp
    break
  if tmp % 10 != 0:
    d.append(tmp * 10 + (tmp % 10 - 1))
  d.append(tmp * 10 + tmp % 10)
  if tmp % 10 != 9:
    d.append(tmp * 10 + (tmp % 10 + 1))
print(ans)
