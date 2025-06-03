import math
x = int(input())
n = 100
y = 0

while x > n:
    # 小数点以下切り捨て
    n += n // 100
    y += 1

print(y)