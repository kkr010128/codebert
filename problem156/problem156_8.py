X=int(input())
a=True
while a==True:
    for i in range(-1000,1001):
        for j in range(i,1001):
            if j**5-i**5==X:
                print(j,i)
                exit()
