def gcd(a,b):
    x = max(a,b)
    y = min(a,b)

    while True:
        n = x%y
        if n == 0:
            print(y)
            break
        else:
            x = y
            y = n


a,b = map(int,input().split())
gcd(a,b)