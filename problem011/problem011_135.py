def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    while y > 0:
        r = x % y
        x = y
        y = r

    return print(x)

x_y = input()
tmp = list(map(int, x_y.split()))
x = tmp[0]
y = tmp[1]
gcd(x, y)
