def gcm(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x==y:
        return x
    if x>y:
        return gcm(x%y,y)
    else:
        return gcm(y%x,x)


x, y = list(map(int, input().split()))

print(gcm(x, y))
