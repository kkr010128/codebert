def gcd2(x,y):
    if y == 0: return x
    return gcd2(y,x % y)

def lcm2(x,y):
    return x // gcd2(x,y) * y

a,b = map(int,input().split())
print(lcm2(a,b))