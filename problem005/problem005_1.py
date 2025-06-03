while True:
    try:
        a, b = map(int, raw_input().split())
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a%b)
        g = gcd(a,b)
        l = a*b/g
        print g, l
    except:
        break