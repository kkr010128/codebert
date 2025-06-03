x,k,d = map(int, input().split())
x = abs(x)
if x - d*k >= 0:
    print(abs(x-d*k))
else:
    a = x // d
    if k % 2 == 0:
        if a % 2 == 0:
            print(abs(x - d*a))
        else:
            print(abs(x - d * (a+1)))
    else:
        if a % 2 == 0:
            print(abs(x - d * (a + 1)))
        else:
            print(abs(x - d * a))

