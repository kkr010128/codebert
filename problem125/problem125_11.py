x=int(input())
for m in range(1,180):
    if 360*m%x==0:
        print(360*m//x)
        exit(0)