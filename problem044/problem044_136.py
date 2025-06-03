cnt = 0

a, b, c = map(int, input().split())

if (a >= 1 and a <= 10000) and (b >= 1 and b <= 10000) and (c >= 1 and c <= 10000):
    if a <= b:  
        for i in range(a, b+1):
            if c % i == 0:
                cnt += 1
        print("{0}".format(str(cnt)))
    else:
        pass
else:
    pass