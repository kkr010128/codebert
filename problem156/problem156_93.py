x = int(input())
a = 0
while True:
    for b in range(a):
        if abs(a ** 5 - b ** 5) == abs(x):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                exit()
            else:
                print(-a, -b)
                exit()
        elif abs(a ** 5 + b ** 5) == abs(x):
            if a ** 5 + b ** 5 == x:
                print(a, -b)
                exit()
            else:
                print(-a, b)
                exit()
    a += 1