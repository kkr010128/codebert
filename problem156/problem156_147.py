x = int(input())

a = 0
while True:
    b = a
    while a**5 - b**5 <= x:
        if a**5 - b**5 == x:
            print(a, b)
            exit()
        b -= 1
    a += 1
