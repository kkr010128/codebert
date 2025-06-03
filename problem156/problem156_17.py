x = int(input())
for i in range(1,1500):
    for j in range(-1000,1000):
        y = i**5 - j**5
        if x == y:
            print(i,j)
            exit()