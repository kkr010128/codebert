x = int(input())

for a in range(-501, 501):
    for b in range(-501, 501):
        if a**5 - b** 5 == x:
            print (a, b)
            exit()