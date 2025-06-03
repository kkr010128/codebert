X = int(input())

for x in range(1, 361):
    if x * X % 360 == 0:
        print(x)
        exit()
