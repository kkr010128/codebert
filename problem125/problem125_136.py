X = int(input())
ret = 0
cur = 0
while True:
    ret += 1
    cur += X
    if cur % 360 == 0:
        print(ret)
        break
