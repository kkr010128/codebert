n = int(input())
for i in range(1000):
    for j in range(-1000,1000):
        if (i**5-j**5)==n:
            print(i,j)
            exit()