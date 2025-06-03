def F(x, y):
    if x % y == 0:
        return y
    return F(y, x % y)
while True:
    try:
        x, y = map(int,input().split())
        print('{0} {1}'.format(F(x, y), int(x * y / F(x, y))))
    except EOFError:
        break

