from collections import deque
N = int(input())
C = input()
r = deque()
lr = 0
for i in range(N):
  if C[i] == 'R':
    lr += 1
    r.append(i)
ans = 0
for i in range(N):
  if lr == 0:
    break
  if C[i] == 'W':
    if i < r[-1]:
      ans += 1
      r.pop()
      lr -= 1
    else:
      break
print(ans)