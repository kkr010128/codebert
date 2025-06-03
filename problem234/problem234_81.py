from collections import defaultdict
n = int(input())
cnt = 0
d = defaultdict(int)
for i in range(1,n+1):
  a = int(str(i)[0])
  b = int(str(i)[-1])
  if b != 0:
    d[a*10+b] += 1
for i in range(1,n+1):
  a = int(str(i)[0])
  b = int(str(i)[-1])
  if b != 0:
    cnt += d[b*10+a]
print(cnt)