import fractions

a,b = map(int,input().split())

def lcm(x,y):
    z = int(x*y/fractions.gcd(x,y))
    return z
    
print(lcm(a,b))