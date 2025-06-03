x = int(input().strip())

for i in range(120):
    for j in range(120):
        y = i**5 + j**5
        z = i**5 - j**5
        if z == x:
            a = i
            b = j
            print("{} {}".format(a, b))
            exit()
        if y == x:
            a = i
            b = -j
            print("{} {}".format(a, b))
            exit()

