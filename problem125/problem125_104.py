X=int(input())
for i in range(1,10000):
    if (i*X)%360==0:
        print(i)
        break