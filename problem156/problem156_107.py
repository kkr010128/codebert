x = int(input())
y = 10**4

for i in range(y):
    for j in range(-y,y):
        if i ** 5 - j ** 5 == x:
            print(i, j)
            exit()