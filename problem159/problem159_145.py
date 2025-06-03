import math
X = int(input())
V = 100
cnt = 0
while V < X:
    V = V * 101 // 100
    cnt += 1
print(cnt)
