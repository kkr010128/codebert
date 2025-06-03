X = int(input())
cnt = 1
while True:
    tmp = X * cnt
    m, d = divmod(tmp, 360)
    if m >= 1 and d == 0:
        print(cnt)
        exit()
    cnt += 1