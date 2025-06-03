a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def cal(c):
    d = []
    while c%2 == 0:
        d.append(2)
        c //= 2
    f = 3
    while f**2 <= c:
        if c%f == 0:
            d.append(f)
            c //= f
        else:
            f += 2
    if c != 1:
        d.append(c)
    return d
    
c = gcd(a, b)
d = cal(c)
print(len(set(d))+1)
