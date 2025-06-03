N, M = map(int, input().split())
S = input()
if N <= M:
  print(N)
  exit()
if '1'*M in S:
  print(-1)
  exit()

from collections import deque
count = deque([])
for k in range(M+1):
  if S[k] == '1':
    count.append(-1)
  else:
    count.append(k)
sgn = deque([])
k = 0
while k < N:
  k += 1
  if S[k] == '0':
    sgn.append(M)
  else:
    d = 0
    while k < N:
      if S[k] == '1':
        k += 1
        d += 1
        continue
      else:
        break
    while d > 0:
      sgn.append(M-d)
      d -= 1
    sgn.append(M)
now = M
while now < N:
  now += 1
  a = sgn.popleft()
  if S[now] == '1':
    count.append(-1)
  else:
    count.append(a)
count = list(count)  
c = 0
ans = ''
while c < N:
  ans = str(count[-1-c]) + ' ' + ans
  c += count[-1-c]

print(ans)