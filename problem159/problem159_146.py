X = int(input())
a = 100
for i in range(1, 100000):
    a = a * 101 // 100
    if a >= X:
        print(i)
        exit()
