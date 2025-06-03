try:
    X_s,Y_s,Z_s = input().split(' ')
    X=int(X_s)
    Y=int(Y_s)
    Z=int(Z_s)
    
    if X>=1 and X<=100 and Y>=1 and Y<=100 and Z>=1 and Z<=100:
        
        A=X
        B=Y
        C=Z
        
        temp=B
        B=A
        A=temp
        
        temp=C
        C=A
        A=temp
        
        print(A,'',B,'',C)
        
except Exception as e:
    print(e)