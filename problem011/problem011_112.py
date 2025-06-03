def gcd(a,b):
    if a == 0:
        return b
    else:
        g = gcd(b%a,a)
        return g

n1,n2 = map(int,raw_input().split())
print gcd(n1,n2)