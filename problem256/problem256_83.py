def gcd(m,n):
    x = max(m,n)
    y = min(m,n)
    while x%y != 0:
        z = x%y
        x = y
        y = z
    else:
        return y
def lcm(m,n):
    return int(m * n /gcd(m,n))

A,B = map( int ,input().split())
print(lcm(A,B))