while True:
    try:
        a, b = map(int, input().split())
        if a < b:
            b, a = a, b
        x, y = a, b
        while b: a, b = b, a%b
        gcd = a
        lcm = (x*y)//gcd
        print(gcd, lcm)
    except:
        break