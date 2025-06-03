def gcd(a,b):
    r = a%b
    if r==0:
        return b
    else:
        return gcd(b,r)

def lcm(x,y):
    return (x * y) // gcd(x, y)
n,m=map(int, input().split())
print(lcm(n,m))
