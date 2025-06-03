# 1%
import math

N = int(input())
x = 100
ans = 0
while x < N:
    x += x // 100
    ans += 1

print(ans)
