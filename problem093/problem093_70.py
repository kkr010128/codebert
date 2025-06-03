from collections import defaultdict
def f(s):
  return int(s) - 1

N, K = map(int, input().split())
P = list(map(f, input().split()))
C = list(map(int, input().split()))

loop = []

first = -1
x = -1
loop_mem = []
cnt = 0
score = 0

rem = set(range(N))

while len(rem) > 0:
  if first < 0:
    first = rem.pop()
    x = first
  loop_mem.append(x)
  if x != first:
    rem.remove(x)
  cnt += 1
  score += C[x]
  if first != P[x]:
    x = P[x]
  else:
    loop.append((loop_mem, cnt, score))
    first = -1
    loop_mem = []
    cnt = 0
    score = 0

ans = -1e10
for loop_mem, cnt, score in loop:
  imax = [-1e10 for _ in range(cnt)]
  imax[0] = 0
  for x in loop_mem:
    tmp = 0
    for j in range(1, cnt):
      tmp += C[x]
      imax[j] = max(imax[j], tmp)
      x = P[x]
  for j in range(2, cnt):
    imax[j] = max(imax[j-1], imax[j])
  if score <= 0:
    ans = max(ans, imax[-1])
  else:
    M = K // cnt
    m = K % cnt
    if M >= 1:
      tmp = max(score * M + max(imax[m], 0), score * (M-1) + imax[-1])
    else:
      tmp = imax[m]
    ans = max(ans, tmp)

print(ans)
