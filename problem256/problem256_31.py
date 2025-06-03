A,B=map(int,input().split())
for i in range(1,B+1):
    if((A*i)%B==0):
        print(A*i)
        exit()