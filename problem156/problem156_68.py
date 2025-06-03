x = int(input())
for i in range(1000):
    for j in range(i):
        if i ** 5 - j ** 5 == x:
            print(i, j)
            exit()
        if i ** 5 + j ** 5 == x:
            print(i, -j)
            exit()
