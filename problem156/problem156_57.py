x = int(input())
for i in range(1,121):
    for j in range(-121,121):
        if x == i**5 - j**5:
            print(i,j)
            exit()
