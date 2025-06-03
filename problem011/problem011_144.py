def gcd(x,y):
    if y==0:
        return x
    else:
        x=x%y
        return gcd(y,x)

A=list(map(int,input().split(' ')))
print(gcd(A[0],A[1]))
