import fractions

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

A,B=map(int,input().split())    
print(lcm_base(A,B))