def gcd(X,Y):
    x = X
    y = Y
    if y > x:
        x,y = y,x
    while x % y:
        x,y = y,x%y
    return y

number = [int(i) for i in input().split()]
print(gcd(number[0],number[1]))