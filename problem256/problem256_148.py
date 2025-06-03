
def lcm(x, y):
    from fractions import gcd
    return (x * y) // gcd(x, y) 

a,b = map(int,input().split())

print(lcm(a,b))