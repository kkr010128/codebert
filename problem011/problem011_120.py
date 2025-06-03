def gcd(a,b):
    if a>b:
        x=a
        y=b
    else:
        x=b
        y=a

    if y==0:
        return x
    else:
        return gcd(y,x%y)

p,q=[int(i) for i in input().split(" ")]
print(gcd(p,q))