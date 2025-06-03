a,b = map(int, input().split())

def gcd(x, y):
    if y < x:
        x,y = y,x
    while x%y != 0:
        x,y = y,x%y
    return y

def lcm(x, y):
    return (x*y)//gcd(x,y)

print(lcm(a,b))