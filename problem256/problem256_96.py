A, B = list(map(int,input().split()))

def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def lcm_(x,y):
    return (x * y) // gcd_(x, y)

print(lcm_(A, B))