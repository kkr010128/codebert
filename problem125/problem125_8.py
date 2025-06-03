X=int(input())

for i in range(1,180):
    if (i*360%X==0):
        print((i*360)//X)
        exit()