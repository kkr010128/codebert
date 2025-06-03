def gcd(x, y):
    while y != 0:
        x,y = y, x % y
    return x

A = list(map(int,input().split()))
print(gcd(A[0], A[1]))