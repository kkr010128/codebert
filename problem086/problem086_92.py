import math

def solve(n,x,t):

    if n%x != 0:
        return (math.ceil(n/x))*t

    else:
        return (n//x)*t

n,x,t = map(int, input().strip().split())
print(solve(n,x,t))