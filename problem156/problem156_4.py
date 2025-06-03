X = int(input())
for a in range(1, 1000):
    a5 = a**5
    for b in range(-a+1, a):
        b5 = b**5
        if a5-b5 == X:
            print(a, b)
            exit()
