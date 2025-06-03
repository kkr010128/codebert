X,K,D = map(int,input().split())

y = abs(X)//D

if K<=y:
    print(abs(abs(X)-K*D))

else  :
    a = (abs(X)-y*D)
    b = (abs(X)-(y+1)*D)
    
    C = abs(a)
    D = abs(b)
    
    if (K-y)%2==0:
        print(C)
    else:
        print(D)


#print(y+1)
#print(1000000000000000)