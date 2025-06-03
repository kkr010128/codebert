a,b=map(int,input().split())
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
l=gcd(a,b)
print(int(a*b/l))
