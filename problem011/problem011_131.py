def gcd(x,y):
    a=max(x,y)
    b=min(x,y)
    if a%b==0:
        return b
    else:
        return gcd(a%b,b)
A,B=map(int,input().split())
print(gcd(A,B))

