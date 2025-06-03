N = int(input())
if N % 2 == 1:
    print(0)
else:
    cnt = 0
    for i in range(0,30):
        tmp = 10*(5**i)
        a = N // tmp
        cnt += a

    print(cnt)