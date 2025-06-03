import sys

H = int(next(sys.stdin.buffer))

ans = 0
i = 1
while H > 0:
  H //= 2
  ans += i
  i *= 2

print(ans)