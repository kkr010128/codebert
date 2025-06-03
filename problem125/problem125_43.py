# coding:utf-8
x = int(input())
r = 0
for k in range(360):
    r += x
    if r % 360 == 0:
        break
print(k + 1)
