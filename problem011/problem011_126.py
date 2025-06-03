def gcd(a,b):
    if b == 1:
        return 1
    elif b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int, raw_input().split(' '))
if a > b:
    print gcd(a,b)
else:
    print gcd(b,a)