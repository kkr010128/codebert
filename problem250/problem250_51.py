X=int(input())
x=0
for j in range(X,10**6):
    for i in range(j-1,0,-1):
        if i==1:
            print(j)
            x=1
        elif j%i==0:
            break
    if x==1:
        break