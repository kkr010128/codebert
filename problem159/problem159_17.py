import math
x = int(input())
a = 100
cnt = 0
while(1):
    cnt += 1
    a += a//100
    if a >= x:
        break
print(cnt)
