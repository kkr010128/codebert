X = int(input())
tmp = 360
while True:
    if tmp % X == 0:
        print(tmp//X)
        exit()
    else:
        tmp+= 360