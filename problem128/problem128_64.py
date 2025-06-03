X,N=map(int,input().split())
p=list(map(int,input().split()))
for i in range(102):
    if (X-i)not in p:
        print(X-i)
        exit()
    elif (X+i)not in p:
        print(X+i)
        exit()