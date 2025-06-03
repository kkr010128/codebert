import math

x = int(input())
n = 100
i = 0
while n < x:
    # 複利の計算方法がわかっていない
    n = n * 101 // 100
    i += 1
print(i)