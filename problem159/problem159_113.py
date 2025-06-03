import math
x = int(input())

ans = 0
y = 100
while y < x:
    y += y//100
    ans += 1
print(ans)