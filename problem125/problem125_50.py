X=int(input())
i=1
while True:
    if (X*i)%360==0:
        print(i)
        exit()
    i+=1
