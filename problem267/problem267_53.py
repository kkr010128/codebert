import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

ans = 0

numlist = [[] for i in range(10)]
for i in range(len(S)):
  numlist[int(S[i])].append(i)

ans = 0
import bisect
for i in range(1000):
  target = str(i).zfill(3)
  now = 0
  for j in range(len(target)):
    tar = int(target[j])
    pos = bisect.bisect_left(numlist[tar], now)
    if pos >= len(numlist[tar]):
      break
    now = numlist[tar][pos] + 1
  else:
    ans += 1

print(ans)