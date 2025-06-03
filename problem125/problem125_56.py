X = int(input())

cnt = 0
x = 0
while True:
    x += X
    cnt += 1
    if x % 360 == 0:
        print(cnt)
        exit()
