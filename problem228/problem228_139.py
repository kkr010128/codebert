import math
h = int(input())
cnt = 0

while h > 1:
  h = h // 2
  cnt += 1

ans = 0

for i in range(cnt+1):
  ans += 2 ** i

print(ans)