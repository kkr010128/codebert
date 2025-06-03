import sys

A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for e in sys.stdin:
  c.append(list(map(int, e.split())))

ans = min(a) + min(b)

for i in range(len(c)):
  temp_val = a[c[i][0]-1] + b[c[i][1]-1] - c[i][2]
  if temp_val < ans:
    ans = temp_val

print(ans)