import fractions
A,B=map(int,input().split())

def lcm(x,y):
    return int((x*y)/fractions.gcd(x,y))

print(lcm(A,B))