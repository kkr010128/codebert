x = int(input())
if 360 % x == 0:
    print(360//x)
else:
    for i in range(1, 10000):
        if x*i % 360 == 0:
            print(i)
            exit()