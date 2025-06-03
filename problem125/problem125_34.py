x = int(input())

idx = 0
tmp = 0
while 1:
    tmp += x
    idx += 1
    if tmp % 360 == 0:
        break

print(idx)
